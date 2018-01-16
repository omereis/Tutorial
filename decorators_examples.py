def parent(num):
#    print("Printing from the parent() function.")

    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

#    print(first_child())
#    print(second_child())
    try:
        assert num == 10
        return (first_child)
    except AssertionError:
        return (second_child)

def test_parent():
    x = parent(11)
    y = parent(10)
    print(x)
    print(x())
    print(y)
    print(y())

def my_decorator(some_function):

    def wrapper():
        num = 10
        if (num == 10):
            print("yes")
        else:
            print("no")
        some_function()
        print("Something is happening after some_function() is called.")
    return wrapper

def just_some_function():
    print("Wheee!")

if __name__ == "__main__":
    try:
        my_decorator()
#        test_parent()
#        just_some_function = my_decorator(just_some_function)
#        just_some_function()

    except Exception as excp:
        print ("Error:\n" + str(excp.args))
