import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--port", type=int, default=5000)
parser.add_argument("-H", "--host", type=str, default='0.0.0.0')

args = parser.parse_args()
print(f'Port {args.port}')
print(f'Host {args.host}')

