num = int(input("ENTER A NUMBER-:"))
method = int(input("1/2-:"))
if method == 1:
    reverse = 0
    while num > 0:
        remainder = num % 10
        reverse = (reverse * 10) + remainder
        num = num // 10

    print(reverse)
if method == 2:
    print(str(num)[::-1])
