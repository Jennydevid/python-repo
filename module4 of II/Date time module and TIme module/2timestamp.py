#timestamp is the no. of seconds since jan 1 1970

from datetime import date   
import time

timestamp = time.time()   #gives the time since 1970 in seconds
print(timestamp)
date = date.fromtimestamp(timestamp)   #getting the current date from seconds till now
print(date)