class Super:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "My name is " + self.name + "."


class Sub(Super):
    def __init__(self, name):
        Super.__init__(self, name)  #calling the constructor of superclass using className
        super().__init__(name)      #calling the constructor of superclass using super(0 fun)


obj = Sub("Andy")

print(obj)