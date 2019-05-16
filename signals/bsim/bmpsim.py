import time

def sim_b (t):
    time.sleep(t)

if __name__ == "__main__":
    import argparse
    sim_b
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", type=int, default=5)
    args = parser.parse_args()
    sim_b(args.time)
    print('Done')


