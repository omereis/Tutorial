import asyncio
import websockets
import getopt, sys

host='localhost'
port='8765'
opts=""

try:
    if len(sys.argv) > 0:
        print (sys.argv[1:])
        opts, args = getopt.getopt(sys.argv[1:], "h:p:", ["host", "port"])

except getopt.GetoptError as err:
    # print help information and exit:
    print(err) 
for o,a in opts:
    if o in ('-p', '-port'):
        port = a
    elif o in ('-h', '-host'):
        host = a 

async def hello():
    address = 'wss://{}:{}'.format(host,port)
    #print ('address: "{}"'.format(address))
    #async with websockets.connect(address) as websocket:
    #async with websockets.connect('{}:{}'.format(host,port)) as websocket:
    async with websockets.connect(address) as websocket:
    #async with websockets.connect('ws://ncnr-r9nano.campus.nist.gov:8765') as websocket:
    #async with websockets.connect('ws://localhost:8765') as websocket:
    #async with websockets.connect('ws://0.0.0.0:8765') as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print("name: {}".format(name))

        greeting = await websocket.recv()
        print("{}".format(greeting))

asyncio.get_event_loop().run_until_complete(hello())
