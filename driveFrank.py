import pygame
import time
import random

import zmq, yaml
from multiprocessing import Process


# Server process.
def server(port, send_msg, recv_msg):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:%d" % (port,))
    while True:
        # print send_msg[0]
        recv_msg[0] = socket.recv()
        send_msg[0] += 1
        print recv_msg[0]
        i = 0
        while i < 10000:
            i += 1
        socket.send_json(send_msg[0])


send_msg = [10]
recv_msg = [None]


# Doesn't do anything.
def init():
    pass

# Sends a message. 
def send(msg):
    send_msg[0] = msg

# Receives a message
def recv():
    return recv_msg[0]

port = 12345

remoteIP = "192.168.0.1"

send_process = Process(target=server, args=(port, send_msg, recv_msg))
send_process.start()








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
    send(throttles)
    print recv()
    # print throttles
    # time.sleep(.05)