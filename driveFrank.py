import pygame
import time
import random
import ansible
import zmq, yaml
from multiprocessing import Process
import thread

# Server process.
def server(port, send_msg, recv_msg):
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:%d" % (port,))
    while True:
        # print send_msg[0]
        recv_msg[0] = socket.recv()
        #send_msg[0] += 1
        send_msg_2.msg[0] += 1
        print recv_msg[0]
        i = 0
        #while i < 10000:
        #    i += 1
        socket.send_json(send_msg)
        time.sleep(.3)

send_msg = [0,0]
recv_msg = [None]

class Holder:
    def __init__(self, val):
        self.msg = val

send_msg_2 = Holder([0,0])

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
x = 1
remoteIP = "192.168.0.1"

#send_process = Process(target=server, args=(port, send_msg, recv_msg))
#send_process.start()
send_thread = thread.start_new_thread(server, (port, send_msg, recv_msg))

"""
while(True):
    print send_msg, "msg"
    print send_msg_2.msg, "msg2"
    time.sleep(1)
"""



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
        #if throttles[i] > .7:
        #    throttles[i] = .7
        #if throttles[i] < -.7:
        #    throttles[i] = -.7
    # for i in range(len(gs)):
    #     print gs[i].read_encoder()
    #     gs[i].set_target(100.0*throttles[i])
    send(throttles)
    print throttles
    #ansible.send(throttles)
    print recv()
    # print throttles
    time.sleep(.05)

