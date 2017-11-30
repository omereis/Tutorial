class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

x = MyClass()
y = MyClass()

y.variable = "yackity"

# Then print out both values
print(x.variable)
print(y.variable)
