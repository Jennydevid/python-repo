# s = 'abcdef'
# print(s[::2])

# import os

# os.mkdir('pictures')
# os.chdir('pictures')
# os.mkdir('thumbnails')
# os.chdir('thumbnails')
# os.mkdir('tmp')
# os.chdir('../')

# print(os.getcwd())

# x = '\\\'
# print(len(x))

# class A:
#     def __init__(self, v=1):
#         self.v = v

#     def set(self, v = 2):
#         self.v += v
#         return self.v

# a = A()
# b = a 
# b.set()
# print(a.v)

# try:
#     raise Exception
# except:
#     print("c")
# except BaseException

# import math
# print(dir(math))

# class A:
#     def __init__(self) :
#         pass

# a = A(1)
# print(hasattr(a,"A"))

# class A:
#     A = 1
#     def __init__(self) :
#         self.a = 0

# print(hasattr(A, 'a'))

# class A:
#     def __init__(self):
#         self._a = 2

# a = A()
# print(a._a).

# from re import S


# str = 'abcdef'

# def fun(s):
#     del s[2]
#     return S
# print(fun(str))

# lst = [[],[],[]]
# print(len(lst))

# t = (1,2,3,4)
# t = t[-2:-1]
# print(t)
# t = t[-1]
# print(t)

my_list = [[c for c in range(r)] for r in range(3)]
print(my_list)
for element in my_list:
    if len(element) < 2:
        print()