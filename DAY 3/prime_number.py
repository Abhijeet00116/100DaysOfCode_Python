num = int(input("ENTER A NUMBER -:"))
flag = 0
if num >= 2:
    for i in range(2, int(pow(num, 0.5) + 1)):
        if num % i == 0:
            flag = 1
            break
if flag == 1:
    print('Not Prime')
else:
    print("Prime")
