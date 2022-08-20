def read_int(prompt, min, max):
    while True:
        try:
            if min <= prompt <= max:
                return result
        except ValueError:
            print("Error: wrong input")
        except:
            print("Error: the value is not within permitted range (-10..10)")
    

v = read_int(int(input("Enter a number from -10 to 10: ")), -10, 10)

print("The number is:", v)
