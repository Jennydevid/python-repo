class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1   #class_name.variable_name will set the counter for all the instances created
                                    #if used as objectName.VariableName will set the counter separately for every object

example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)  #__dict__ for object
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

print(ExampleClass.__dict__)  # __dict for class
