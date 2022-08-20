#the situation in which the subclass changes the behaviour of the super class
# is polymorphism
class One:
    def do_it(self):
        print("do_it from One")

    def doanything(self):
        self.do_it()

class Two(One):
    def do_it(self):
        print("do_it from Two")

one = One()
two = Two()

one.doanything()
two.doanything()