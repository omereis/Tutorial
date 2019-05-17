import subprocess
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--time", type=int, default=5)
    args = parser.parse_args()
    print(f'args.time={args.time}')
    bmpsim_args = f'-t {args.time}'
    print(f'bmpsim_args={bmpsim_args}')
    subprocess.Popen (['python','bmpsim.py'])

