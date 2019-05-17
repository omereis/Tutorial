from multiprocessing import Process, Queue
import random

def rand_num():
    name = multiprocessing.current_process().name
    num = random.random()
    print(f'Process {name}: {num}')

if __name__ == "__main__":
    queue = Queue()

    processes = [Process(target=rand_num, args=()) for x in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
