from os import strerror

ba = bytearray(10)

for i in range(len(ba)):
    ba[i] = ord('a') + i

try:
    file = open("Binary.txt",'wb')
    result = file.write(ba)   #the function will return the number of bytes written in the file
    file.close()
    print("return value of write() fun: ",result)
except IOError as e:
    print("IOError: ",strerror(e.errno))
