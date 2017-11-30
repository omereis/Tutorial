class MyClass:
    some_var = "blah"

    def function (self):
        print ("This is a message from inside the class")

    def f2(self, txt, txt2):
        print(self.some_var + "\n" + txt + "\n2:\t" + txt2)

    def f1(self, txt1):
        self.f2("From f1", "2nd param")
    
print ("Hello, Python!, v0.2")

myobj = MyClass()
print(myobj.some_var)
myobj.f1("jjk")
myobj.function()