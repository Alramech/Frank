import pygame
import time
import ansible

pygame.init()
pygame.joystick.init()
j = pygame.joystick.Joystick(0)
j.init()    

while True:
    pygame.event.get()

    throttles = list((j.get_axis(1), -j.get_axis(4)))

    for i in range(len(throttles)):
        if abs(throttles[i]) < .15:
            throttles[i] = 0
    # for i in range(len(gs)):
    #     print gs[i].read_encoder()
    #     gs[i].set_target(100.0*throttles[i])
    ansible.send(throttles)
    print throttles
    time.sleep(.05)