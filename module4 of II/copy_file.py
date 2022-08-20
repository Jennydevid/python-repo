from os import strerror


srcFile = input("Enter the file to be copied: ")
try:
    sf = open(srcFile, 'rb')
except IOError as e:
    print("IOError: ",strerror(e.errno))
    exit(e.errno)  
       #exit fun stops the program execution and returns the completion code to us
       # any number other than 0 passed as a parameter,says that a problem was encountered
       #passed the errno to specify the problem

dsFile = input("What is the destination file? ")
try:
    df = open(dsFile, 'wb')
except IOError as ex:
    print("IOError: ",strerror(ex.errno))
    exit(ex.errno)

buffer = bytearray(65536)
total = 0

try:
    readin = sf.readinto(buffer)
    while readin > 0:
        written = df.write(buffer[:readin])
        total += written
        readin = sf.readinto(buffer)
except IOError as e:
    print("IOError: ", e.errno)

print(total, "bytes copied successfully!!")
sf.close()
df.close()