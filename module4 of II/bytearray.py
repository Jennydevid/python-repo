a = bytearray(10)
for i in range(len(a)):
    a[i] = 10 -i

for j in range(len(a)):
    print(hex(a[j]), end="  ")