class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):  #extending the Stack class
    def __init__(self):
        Stack.__init__(self)   # called the constructor of super class
        self.__counter = 0     # declared a private variable for the subclass
    #
    # Fill the constructor with appropriate actions.
    #

    def get_counter(self):
        return self.__counter
    #
    # Present the counter's current value to the world.
    #

    def pop(self):
        val = Stack.pop(self)
        self.__counter += 1
    #
    # Do pop and update the counter.
    #
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
