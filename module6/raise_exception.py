def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise
        # raise keyword raises the same error again i.e zero error here

try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")
