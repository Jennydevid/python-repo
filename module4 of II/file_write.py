from os import strerror

try:
    s = open('write.txt','w')
    for i in range(10):
        st = "* line "+ str(i+1)+"\n"
        s.write(st)
    s.close()
except IOError as exe:
    print("The IOError is: ",strerror(exe.errno))
