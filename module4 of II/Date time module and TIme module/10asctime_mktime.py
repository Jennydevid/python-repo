import time

obj = time.gmtime()  #getting struct_time object

print(time.asctime(obj))   # returns the string of the struct_time object

print(time.mktime(obj))    # converts the struct_time object to seconds
