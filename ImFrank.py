from grizzly import *
import time
import zmq
from multiprocessing import Process


# Client process.
def client(port, send_msg, recv_msg):
    leftMotor = Grizzly(0xF-0xB)
    leftMotor.set_mode(ControlMode.NO_PID, DriveMode.DRIVE_BRAKE)
    leftMotor.limit_acceleration(60)
    leftMotor.limit_current(5)
    rightMotor = Grizzly(0xF-0x9)
    rightMotor.set_mode(ControlMode.NO_PID, DriveMode.DRIVE_BRAKE)
    rightMotor.limit_acceleration(60)
    rightMotor.limit_current(5)

    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://%s:%d" % (remoteIP, port))
   
    print 'Waiting for client to send.' 
    while True:
      try:
        socket.send_json(send_msg[0])
        send_msg[0] += 1
        recv_msg = socket.recv_json()
        print recv_msg[0]
        recv_msg = recv_msg[0]
        leftMotor.set_target(float(recv_msg[0])*100)
        rightMotor.set_target(float(recv_msg[1])*100)
        time.sleep(.05)
      except BaseException as e:
        print e
        
        time.sleep(1)
        exit(0)
send_msg = [0]
recv_msg = [None]


# Doesn't do anything.
def init():
    pass

# Sends a message. 
def send(msg):
    send_msg[0] = msg

# Receives a message
def recv():
    return recv_msg

port = 12345

remoteIP = "192.168.0.100"

#send_process = Process(target=client, args=(port, send_msg, recv_msg))
#send_process.start()

client(port, send_msg, recv_msg)





# addrs=Grizzly.get_all_ids()
# gs=[]
# for addr in addrs:
#     g = Grizzly(addr)
#     g.set_mode(ControlMode.NO_PID, DriveMode.DRIVE_COAST)
#     g.limit_acceleration(142)
#     g.limit_current(10)
#     gs.append(g)

# for g in gs:
#     g.set_target(0)

# while True:
#     data = 0
#     send(data)
#     data += 1
#     command = ansible.recv()
#     print command
#     if command:
#         print "Command!"
#         print command
#         # for i in range(len(command)):
#         #     if abs(command[i]) < .15:
#         #         command[i] = 0
#         for i in range(len(gs)):
#             gs[i].set_target(100.0*command[i])
# #    else:
# #       for i in range(len(gs)):
# #           gs[i].set_target(0)
#     time.sleep(.05)
