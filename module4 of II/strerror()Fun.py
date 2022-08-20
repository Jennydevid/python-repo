from os import strerror

try:
    stream = open("closure.py", "r")
except Exception as exc :
    print("Could not open the file due to erron :", strerror(exc.errno))
