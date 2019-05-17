import multiprocessing as mp

def my_func(x):
  print(f'{x}*{x}={x**x}')

def main():
  pool = mp.Pool(mp.cpu_count())
  result = pool.map(my_func, [4,2,3])

if __name__ == "__main__":
  main()
