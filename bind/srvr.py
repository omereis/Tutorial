#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

condition = True
while condition:
    #  Wait for next request from client
    message = socket.recv()
    msg = message.decode('utf-8')
    if (msg == 'quit'):
        condition = False
        print("Quit Message")
    print("Received request: %s" % message)
    print("condition: ", condition)
    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client
    socket.send(b"World")

