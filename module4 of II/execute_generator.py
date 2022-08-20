def fun(n):
    for i in range(n):
        yield i

   #let v here is the value returned by yield
for v in fun(5):
    print(v)
