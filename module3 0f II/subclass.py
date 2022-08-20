class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

      
class AddingStack(Stack):
    def __init__(self):   
        Stack.__init__(self)   #the constructor of superclass needs to be called explicitly
        self.__sum = 0     #this is again a private variable
