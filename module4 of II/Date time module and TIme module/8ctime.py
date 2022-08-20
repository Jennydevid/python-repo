import time

samay = time.time()   #time in seconds since 1970
print(time.ctime(samay))

#the ctime function can also be invoked without arguments 
# to get the present time
print(time.ctime())