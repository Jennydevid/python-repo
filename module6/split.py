def my_split(strng):
    lst = []
    word = ""
    strng = strng.strip()
    if strng == "":
        return lst
    strng += " "
    for e in strng:
        if e != " ":
            word += e
        else:
            lst.append(word)
            word = ""
    return lst

# print(my_split("To be or not to be, that is the question"))
# print(my_split("To be or not to be,that is the question"))
print(my_split("   "))
print(my_split(" abc "))
print(my_split("Jyoti is mad"))