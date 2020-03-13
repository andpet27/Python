class MyClass:
    veriable = "blah"

    def function(self):
        print("This is a message inside the class.")

myObjectX = MyClass()
myObjectY = MyClass()

myObjectY.veriable = "new string"

myObjectX.function()
print(myObjectY.veriable)
print(myObjectX.veriable)