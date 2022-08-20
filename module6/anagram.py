#words with same letters rearranged to form new words
def anagrams():
    str1 = input("First string: ")
    str1 = str1.replace(' ','').lower()
    str2 = input("Second string: ")
    str2 = str2.replace(' ', '').lower()
    if str1 == "" or str2 == "":
        print("Not anagrams")
        return 
    str1 = list(str1)
    str1.sort()
    str2 = list(str2)
    str2.sort()
    if "".join(str1) == "".join(str2):
        print("anagrams")
        return 
    print("Not anagrams")

anagrams()