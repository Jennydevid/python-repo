text = input("Any message! ")
cipher = ""
try:
    shift = int(input("Enter a shift value between 1 to 25: "))
except:
    print("Invalid shift value!!")
for char in text:
    if char.isalpha():
        code = ord(char) + shift
        if char.isupper() and code > ord('Z'):
            code -= ord('Z') 
            code += ord('A') - 1
        if char.islower() and code > ord('z'):
            code -= ord('z') 
            code += ord('a') - 1

        cipher += chr(code)
    else:
        cipher += char
print(cipher)