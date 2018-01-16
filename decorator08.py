import time
def timing_function(some_function):
    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper(n=0):
        t1 = time.time()
        some_function(n)
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper


@timing_function
def my_function(n):
    num_list = []
    n = max (n, 1)
    for num in (range(0, n)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))

if __name__ == "__main__":
    try:
        print(my_function(10000000))
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
