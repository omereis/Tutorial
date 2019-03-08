import asyncio
import websockets
import getopt, sys

try:
    if len(sys.argv) > 0:
        print('ARGV      :', sys.argv[1:])
        options, remainder = getopt.getopt(
            sys.argv[1:],
            'h:p:',
            [
            'host=',
            'port='
            ])
except getopt.GetoptError as err:
    print(err) 
    exit(1)
#------------------------------------------------------------------------------
host = 'localhost'
port = 8765
#------------------------------------------------------------------------------
for opt, arg in options:
    if opt in ('-h', '--host'):
        host = arg.strip();
    elif opt in ('-p', '--port'):
        port = arg.strip();
#------------------------------------------------------------------------------
async def hello(websocket, path):
    name = await websocket.recv()
    source = websocket.remote_address
    print ("Just got a message from a client in {}".format(source))
    print(" {}".format(name))
    greeting = "Hello {}, from {}:{}!".format(name, host, port)
    await websocket.send(greeting)
    print(greeting)
#------------------------------------------------------------------------------
print('Host: {}'.format(host))
print('Port: {}'.format(port))
start_server = websockets.serve(hello, host, port)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
