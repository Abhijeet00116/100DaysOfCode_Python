low = int(input("enter the starting range -: "))
up = int(input("enter the ending range -: "))
Sum = 0
for i in range(low, up + 1):
    Sum = Sum + i
print("Sum of Numbers from "+str(low)+" - "+str(up)+" are -: ")
print(Sum)
