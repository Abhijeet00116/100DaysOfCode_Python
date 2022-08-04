while 1:
    value = int(input("ENTER AN INTEGER -: "))
    if value >= 0:
        if value == 0:
            print("ZERO")
        else:
            print("POSITIVE")
    else:
        print("NEGATIVE")
    check = int(input("Want to exit? (0/1)-:"))
    if check == 0:
        exit(0)
