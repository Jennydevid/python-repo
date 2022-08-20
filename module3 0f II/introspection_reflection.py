#accessing the object variables and manipulating them
class Inspect:
    pass

obj = Inspect()
obj.a = 2
obj.b = 3
obj.ireal = 4
obj.i = "Jyoti"
obj.integer = 9
obj.inter = 4.4

def IncIntsI(obj):
    print(obj.__dict__)
    for name in obj.__dict__.keys():    #return the list of attributes in the object
        if name.startswith('i'):  
            val = getattr(obj, name)    # return the value of the attribute of the given object
            if isinstance(val, int):    # checks if the val is of the given type
                setattr(obj, name, val+1)
    print(obj.__dict__)

IncIntsI(obj)
