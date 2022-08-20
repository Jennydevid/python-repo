from datetime import datetime

obj = datetime.strptime('2020/11/12','%Y/%m/%d')
print(obj)
print(type(obj))# the strptime fun creates an object of datetime class


#the strptime fun of time module creates an object of struct_time class
import time

obj2 = time.strptime('2022:01:17  20:25:10','%Y:%m:%d  %H:%M:%S')
print(obj2)
print(type(obj2))