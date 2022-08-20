import time

class short_Nap:
    def nap(self, seconds):
        print("Feeling sleepy!!")
        time.sleep(6)
           #the sleep fun suspends the program execution for given seconds
        print("Had a break... not drowsing any more!!")

s = short_Nap()
s.nap(5)