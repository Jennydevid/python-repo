class Classy:
    pass


print(Classy.__module__)
obj = Classy()
print(obj.__module__)   #__module__ stores the name of the module which has the class definition
                        # if module name is __main__ ,it is not a module but the file currently being run
