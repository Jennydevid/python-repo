from os import strerror

try:
    lcnt = ccnt = 0
    stream = open('closure.py','r')
    line = stream.readline()
    while line != "":
        lcnt += 1
        for c in line:
            print(c, end="")
            ccnt += 1
        line = stream.readline()
    stream.close()
    print("The no of characters are: ", ccnt)
    print("The no of lines are: ", lcnt)
except IOError as e:
    print("IOError: ",strerror(e.errno))