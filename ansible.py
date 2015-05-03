import zmq, yaml
from multiprocessing import Process, Queue
from Queue import Empty

# Sender process.
def sender(port, send_queue):
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.connect("tcp://%s:%d" % (remoteIP, port))
    while True:
        msg = send_queue.get()
        socket.send_json(msg)

# Receiver process.
def receiver(port, recv_queue):
    context = zmq.Context()
    socket = context.socket(zmq.PAIR)
    socket.bind("tcp://0.0.0.0:%d" % port)
    # socket.bind("tcp://%s:%d" % (remoteIP, port))
    while True:
        msg = socket.recv()
        parsed = yaml.load(msg)
        recv_queue.put(parsed)

send_queue = None
recv_queue = None

# Doesn't do anything.
def init():
    pass

# Sends a message. Not blocking.
def send(msg):
    send_queue.put_nowait(msg)

# Receives a message, or None if there is no current message.
def recv():
    try:
        return recv_queue.get_nowait()
    except Empty:
        return None

# Intialize on module import
send_port = 12355
recv_port = 12355

remoteIP = "192.168.0.100"

send_queue = Queue()
recv_queue = Queue()

print "Send:" + str(send_port)
print "Receive:" + str(recv_port)

send_process = Process(target=sender, args=(send_port, send_queue))
# recv_process = Process(target=receiver, args=(recv_port, recv_queue))
send_process.start()
# recv_process.start()
