
import signal  
import time
import os
  
  
def handler(a, b):  # define the handler  
    print("Signal Number:{}, frame: {}".format (a, b))
  
signal.signal(signal.SIGINT, handler)  # assign the handler to the signal SIGINT  
  
print('My PID is:', os.getpid())
while 1:  
    print("Press ctrl + c")  # wait for SIGINT  
    time.sleep(10) 
