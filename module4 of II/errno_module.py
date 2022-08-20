# the module contains errno symbols which helps to detect the error occured
import errno

try:
    stream = open("subclass.py", "r")
except Exception as exc:
    # the errno is the attribute of the IOError object
    if exc.errno == errno.ENOENT:
        print("No such file or directory!!")
    elif exc.errno == errno.EISDIR:
        print("It is a directory!!")
    else:
        print("Could not open the file!!")