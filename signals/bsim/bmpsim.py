import time
import os

def sim_b (t):
    time.sleep(t)


if __name__ == "__main__":
    import argparse
    #sim_b
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", type=int, default=5)
    args = parser.parse_args()
    print (f'Starting {os.path.basename(__file__)}')
    print(f'Estimated time {args.time} seconds')
    sim_b(args.time)
    print('Done')


