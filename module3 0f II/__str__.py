class Star:
    def __init__(self, name, galaxy):
        self.name = name
        self.galaxy = galaxy
           # the default str fun is used when any class/object is to be presented as a string
           # it is implicitly called when the object name is passed as a parameter to print fun
    def __str__(self):
        return self.name + ' in ' + self.galaxy


sun = Star("Sun", "Milky Way")
print(sun)