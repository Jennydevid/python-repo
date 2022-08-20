from os import strerror

input_file = input("What is the name of the file? ")
dict = {}
try:
    f = open(input_file, 'rt')
    data = f.read()
    data = data.upper()
    for ch in data:
        if ch != " ":
            if ch in dict:
                dict[ch] += 1
            else:
                dict[ch] = 1
except IOError as e:
    print("IOError: ",strerror(e.errno))

for e in dict:
    print(e,"->",dict[e])

