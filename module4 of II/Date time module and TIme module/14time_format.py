#impoprted two classes from the datetime module
from datetime import datetime, time

dt = datetime(2022, 12, 11, 23, 20, 59)
print(dt.strftime('%H:%M:%S'))  
                  #the format is specified using the directives %H, %M etc
print(dt.strftime('%Y : %B : %d -- %H : %M : %S'))

