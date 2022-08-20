def digitOfLife():
    dob = (input("What's your date of birth(YYYYDDMM or YYYYMMDD form): "))
    if not dob.isdigit():
        print("Invalid input!!")
        return
    dob = int(dob)
    while True:
        sum = 0
        while dob != 0:
            r = dob % 10
            sum += r
            dob //= 10
        dob = sum
        if sum < 10:
            print(sum)
            return 
    print(sum)
    return

digitOfLife()