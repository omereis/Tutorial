import signal
import os
import time


def receive_signal(signum, stack):
    print('Received:', signum)
    print('stack: {}', stack)

# Register signal handlers
signal.signal(signal.SIGUSR1, receive_signal)
signal.signal(signal.SIGUSR2, receive_signal)

# Print the process ID so it can be used with 'kill'
# to send this program signals.
print('My PID is:', os.getpid())

n=1
while True:
    print('Waiting...')
    if n % 3 == 0:
        try:
            os.kill(os.getpid(), signal.SIGUSR1)
            print('Sent signal at n={}'.format(n))
        except Exception as e:
            print ('signal bug: {}'.format(e))
    n = n + 1
    time.sleep(3)
