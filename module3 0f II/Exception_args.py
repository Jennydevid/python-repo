# What is the expected output of the following code?

import math

class NewValueError(ValueError):
    def __init__(self, name, color, state):
        self.data = (name, color, state)

try:
    raise NewValueError("Enemy warning", "Red alert", "High readiness")   #object of NewValueError class
except NewValueError as nve:
    # print(nve.args)
    for arg in nve.args:      #args here is the tuple of the arguments of the object
        print(arg, end='! ')