class Classy:
    def visible(self):
        print("visible")
    
    def __hidden(self):     #methods starting with ___are partially hidden
        print("hidden")


obj = Classy()
obj.visible()

try:
    obj.__hidden()   #the hidden method cannot be accessed in noraml way
except:
    print("failed")

obj._Classy__hidden()   #this is property name mangling