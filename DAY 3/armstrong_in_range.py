low, high = map(int, input().split())
for n in range(low, high + 1):
    order = len(str(n))
    Sum = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        Sum += digit ** order
        temp //= 10
    if n == Sum:
        print(n, end=", ")
