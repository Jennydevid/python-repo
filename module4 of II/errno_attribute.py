#errno is the attribute of IOError object
try:
    stream = open("noOfPops.py",'r')
except Exception as exe:
    print("Could not open the file!!")
    print(exe.errno)
