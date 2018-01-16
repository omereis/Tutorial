class C():
    def __str__(self):
        return ("This is __str__ ia C class")
    def __repr__(self):
        return ("This is __repr__ ia C class")

if __name__ == "__main__":
    try:
        c = C()
        print(c)
        print(str(c))
    except Exception as excp:
        print ("Error:\n" + str(excp.args))
