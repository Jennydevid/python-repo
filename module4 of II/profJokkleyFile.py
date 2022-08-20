from os import strerror

#base exception class
class StudentsDataException(Exception):
    pass

class BadLine(StudentsDataException):
    def __init__(self, line, str):
        self.line = line
        self.str = str
        super().__init__(self)

class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


#inserting th data within the file 
file = input("Prof. Jekkly's file!!")
try:
    fo = open(file, 'wt')
    while True:
        data = input('Enter the first name, last name, and points(space separated): ')
        if data == "":
            break
        else:
            fo.write(data+"\n")
    fo.close()
except IOError as exe:
    print("Could not open the file due to IOError: ", strerror(exe.errno))


# raarranging the data of the same file
#dictionary to store the output
dict = {}
try :
    fo2 = open(file, 'r+')
    fo2.write("The total points of students are: \n")
    lines = fo2.readlines()
    if lines == "":
        raise FileEmpty
    for i in range(len(lines)):
        lst = lines[i].split()
        if len(lst) != 3:
            raise BadLine(i+1, lines[i])
        key = lst[0]+ ' '+ lst[1]
        try:
            value = float(lst[2])
        except:
            raise BadLine(i+1, lines[i])
        if key in dict:
            dict[key] += value
        else:
            dict[key] = value
        fo2.write(key+ "->"+ str(dict[key]) + "\n")
    
    fo2.close()
except IOError as e:
    print("Could not append due to the error: ",e)
except BadLine as e:
    print("BadLine error: ", strerror(e.line))
except FileEmpty as e:
    print("File empty error: ",strerror(e.errno))

        