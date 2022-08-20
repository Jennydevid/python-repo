from datetime import date

#creating a date object with given date using fromisoformat function
d = date.fromisoformat('2003 - 11 - 12')  #the fun takes a string as a argument

print(d)

# the same o/p is obtained when a date object is created by the date class only
d1 = date(2003, 11, 12) 
         # the only differernce is it takes three separate arguments not a string
print(d1)