#palindrome string
# text = input("Any string: ")
# text = text.replace(' ','')
# text = text.lower()
# if text == "":
#     print("Not a palindrome!!") 
# print(text)
# reverse = ""
# n = len(text)
# while n > 0:
#     reverse += text[n-1]
#     n -= 1
# print(reverse)
# if text == reverse:
#     print("It's a palindrome!")
# else:
#     print("It's not a palindrome!")
    

#2 method
def palindrome():
    text = input("Any string: ")
    text = text.replace(' ','')
    text = text.lower()
    if text == "":
        return "Not palindrome!"
    l = len(text) - 1
    for f in range(len(text)//2):
        if text[f] == text[l]:
            l -= 1
        else:
            return "Not palindrome!"
             
    return "It's a palindrome"

print(palindrome())


