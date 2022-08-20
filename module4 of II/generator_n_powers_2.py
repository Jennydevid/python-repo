# version 1
def power(n):
    for i in range(n+1):
        yield 2 ** i
        
for v in power(5):
    print(v)

# version 2 using list comprehensiveness
def power(n):
    for i in range(n):
        yield 2 ** i

lst = [i for i in power(5)]
print(lst)

# version 3 using list function
def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
l = list(powers_of_2(4))
print(l)

# version 4 using list in operator
def power(n):
    for i in range(n):
        yield 2 ** i

for i in range(10):  # it will output only those integers from the given range which the power function yields
    if i in power(10):
        print(i)