num = int(input("ENTER A NUMBER-:"))
method = int(input("1/2-:"))
if method == 1:

    reverse = int(str(num)[::-1])

    if num == reverse:
        print('Palindrome')
    else:
        print("Not Palindrome")
if method == 2:
    reverse = 0
    while temp > 0:
        remainder = temp % 10
        reverse = (reverse * 10) + remainder
        temp = temp // 10
    if num == reverse:
        print('Palindrome')
    else:
        print("Not Palindrome")
