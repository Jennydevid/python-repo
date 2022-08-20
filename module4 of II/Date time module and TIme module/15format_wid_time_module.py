import time

timestamp = time.time()
st = time.gmtime(timestamp)  # returns the struct_time object

print(time.strftime('%Y/%m/%d', st))  
        #the strftime of time module requires  a struct_time object as an argument
print(time.strftime('%d--%m--%Y'))
        # when no struct_time object is passed, uses the local time