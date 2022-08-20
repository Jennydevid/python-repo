from os import strerror

fileName = input("What's the name of your file? ")
dict = {}
try:
    f = open(fileName, 'rt')
    for line in f:
        for c in line:
            if c != ' ':
                if c in dict:
                    dict[c] += 1
                else:
                    dict[c] = 1
    f.close()
except IOError as exc:
    print("IOerror: ",strerror(exc.errno))
print('Original: ', dict)
dict2 = sorted(dict, key = lambda x: dict[x], reverse= True)  
                  #the sorted fun returns the sorted list of keys as per the given key fun, 
                  # here as per the key's values
                  # the reverse attr when set to True sorts the iterable in revers order
try:
    h = open(input("File name: ") + ".hist", 'wt')
    for i in dict2:
        cnt = dict[i]
        h.write(i + "->" + str(dict[i]) + "\n")
except IOError as e:
    print("Could not open the file due to: ",strerror(e.errno))