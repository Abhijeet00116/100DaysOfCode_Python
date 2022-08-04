number = int(input("ENTER A NUMBER-:"))
num = number
digit, Sum = 0, 0
length = len(str(num))
for i in range(length):
    digit = int(num % 10)
    num = num / 10
    Sum += pow(digit, length)
if Sum == number:
    print("Armstrong number")
else:
    print("Not Armstrong number")
