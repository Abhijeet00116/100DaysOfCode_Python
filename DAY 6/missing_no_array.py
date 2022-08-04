def missingNumber(a,n):
    s=0
    for i in a:
        s = s+ i
    total_sum = n*(n+1)//2
    actual_sum = s
    missing_value = total_sum - actual_sum
    return missing_value

if __name__=="__main__":
    n = int(input())
    a = list(map(int,input().split()))
    print("\n",a)
    print("\n",missingNumber(a,n))