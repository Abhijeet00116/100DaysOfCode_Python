while 1:
    num = int(input("ENTER A NUMBER -: "))
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")
    check = int(input("Want to exit? (0/1)-:"))
    if check == 0:
        exit(0)
