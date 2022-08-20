def findStrings():
    str1 = input("Any string: ").lower()
    str2 = input("String to search in: ").lower()
    for c in str1:
        if str2.find(c)== -1:
            return False
              #i.e the first string is not found within second
    return True

if findStrings():
    print("Yes!")
else:
    print("No")