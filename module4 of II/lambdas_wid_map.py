lst = [x  for x in range(11) if x % 2 == 0]
print(lst)
lst1 = list(map(lambda x: x * x, lst))
print(lst1)