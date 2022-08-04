num1 = int(input("FIRST NUMBER -: "))
num2 = int(input("SECOND NUMBER -: "))
num3 = int(input("THIRD NUMBER -: "))
if num1 >= num2 and num1 >= num3:
    print(str(num1))
elif num2 >= num1 and num2 >= num3:
    print(str(num2))
else:
    print(str(num3))
