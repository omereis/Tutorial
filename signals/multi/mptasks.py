import multiprocessing
import time
#------------------------------------------------------------------------------
def get_multiprocessing_name():
    return multiprocessing.current_process().name
#------------------------------------------------------------------------------
def worker(num):
    print (f'Worker #{num}')
#------------------------------------------------------------------------------
def worker_a():
    name = get_multiprocessing_name()
    print (f'Starting {name}')
    time.sleep(2)
    print (f'Exiting {name}')
#------------------------------------------------------------------------------
def servicing():
    name = get_multiprocessing_name()
    print (f'Starting {name}')
    time.sleep(2)
    print (f'Exiting {name}')
#------------------------------------------------------------------------------
