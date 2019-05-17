import multiprocessing
from mptasks import servicing, worker_a
import time

if __name__ == '__main__':
    worker_1 = multiprocessing.Process(name='worker_a', target=worker_a)
    worker_2 = multiprocessing.Process(target=worker_a) # use default name
    service = multiprocessing.Process(name='servicing', target=servicing)

    worker_1.start()
    worker_2.start()
    service.start()
    f1 = f2 = f3 = True
    while ((f1 == True) & (f2 == True) & (f3 == True)):
        print('')
        f1 = worker_1.is_alive()
        f2 = worker_2.is_alive()
        f3 = service.is_alive()
        if f1:
            print('worker_1 running')
        if f2:
            print('worker_2 running')
        if f3:
            print('service running')
        if ((f1 == True) & (f2 == True) & (f3 == True)):
            time.sleep(1)
