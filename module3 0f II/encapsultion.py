#the ability to protect information from unauthorized access is called encapsulation
class Stack:
    def __init__(self):
        self.__stack_list = []
                #When any class component has a name starting with two underscores (__), #it becomes private - this means that it can be accessed only from #within the class.this is encapsulation concept

stack_object = Stack()
print(len(stack_object.__stack_list))
