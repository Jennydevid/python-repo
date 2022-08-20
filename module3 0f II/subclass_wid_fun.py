class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0
        
    def push(self, val):
        self.__sum += val
        Stack.push(self, val)
        
    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
        
    def get_sum(self):
        return self.__sum

stack1 = AddingStack()

for i in range(5):
    stack1.push(i)
print(stack1.get_sum())
for i in range(5):
    print(stack1.pop())
