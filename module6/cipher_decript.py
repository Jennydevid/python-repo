#decripting a message through caesar cipher
t = input("Your Messsage! ")
cipher_decript = ""
for char in t:
    if char.isalpha():
        char = char.upper()
        code = ord(char) - 1
        if code < ord('A'):
            code = ord('Z')
    cipher_decript += chr(code)
print(cipher_decript)