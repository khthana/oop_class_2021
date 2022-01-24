class MyClass:
    x = 0
    y = ""

    def __init__(self, anyNumber, anyString):
        self.x = anyNumber
        self.y = anyString

    def __str__(self):
        return 'MyClass(x=' + str(self.x) + ' ,y=' + self.y + ')'


myObject = MyClass(12345, "Hello")

print(myObject.__str__())
print(myObject)
print(str(myObject))

