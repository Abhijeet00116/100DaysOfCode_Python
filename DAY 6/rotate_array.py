a = [int(i) for i in input().strip().split()]  # input list elements
n = len(a)
print()
print(a) # original list
last_element = a[-1]
for i in range(n-1,0,-1):
    a[i] = a[i-1]
a[0] = last_element
print(a) # list after rotation