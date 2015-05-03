import pygame
from grizzly import *
import sys
from IPython.display import display, clear_output
import time
import os 

addrs=Grizzly.get_all_ids()
gs=[] 
for addr in addrs:
    g = Grizzly(addr)
    g.set_mode(ControlMode.NO_PID, DriveMode.DRIVE_COAST)
    g.limit_acceleration(142)
    g.limit_current(10)
    gs.append(g)

for g in gs:
    g.set_target(0)

pygame.init()
pygame.joystick.init()
j = pygame.joystick.Joystick(0)
j.init()    
i=0
while True:
    i+=1
    pygame.event.get()

    throttles = list((j.get_axis(1), -j.get_axis(4)))

    for i in range(len(throttles)):
        if abs(throttles[i]) < .15:
            throttles[i] = 0
    for i in range(len(gs)):
        print gs[i].read_encoder()
        gs[i].set_target(100.0*throttles[i])
    time.sleep(0.01)