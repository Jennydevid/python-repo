def one():
    return "#\n"*5
    
def two():
    return "#"*3 + "\n  #" + "\n###" + "\n#" + "\n###"
    
def three():
    return "#"*3 + "\n  #" + "\n###" + "\n  #" + "\n###"
    
def four():
    return "# #\n"*2 + "#"*3 + "\n  #"*2
    
def five():
    return "#"*3 + "\n#\n"+ "#"*3 + "\n  #\n" + "#"*3
    
def six():
    return "#"*3 + "\n#\n" + "#"*3 + "\n# #\n" + "#"*3
    
def seven():
    return "#"*3 + "\n  #"*4

def eight():
    return ("#"*3 + "\n# #\n")* 2 + "#"*3 

def nine():
    return "#"*3 + "\n# #\n"+ "#"*3 + "\n  #\n" + "#"*3

def zero():
    return "#"*3 + "\n# #"*3 + "\n###"

lst = [zero(), one(), two(), three(), four(), five(), six(), seven(), eight(), nine()]

user_input = int(input("Enter any non-negative integer: "))
reverse = 0
while user_input > 0:
    r = user_input % 10
    reverse = reverse * 10 + r
    user_input //= 10
while reverse > 0:
    r = reverse % 10
    print(lst[r])
    r //=10

