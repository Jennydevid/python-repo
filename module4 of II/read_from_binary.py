from os import strerror

data = bytearray(10)
#using readinto fun
try:
    s = open('Binary.txt','rb')
    result = s.readinto(data)    #the readinto fun will read the contents of the file and return 
                        # them in the data bytearray upto it's length
    s.close()
    print(result)  #the readinto fun will return the number of bytes read 
    print(data)
except IOError as exe:
    print("The error occured is: ", strerror(exe.errno))

#using read() function

# try:
#     f = open('Binary.txt', 'rb')
#     data = bytearray(f.read())
#     f.close()
#     for e in data:
#         print(chr(e), end = " ")
# except IOError as exc:
#     print("IOError: ", strerror(exc.errno))