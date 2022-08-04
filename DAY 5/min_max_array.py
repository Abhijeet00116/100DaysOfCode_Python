def getMinMax(a, n):
    min = max = 0
    p=[]
    a.sort()
    min,max = a[0],a[-1]
    p.append(min)
    p.append(max)

    return p

def main():
    T = int(input()) #Total test Cases
    while(T > 0):
        n = int(input()) # No of test cases inside a Test case
        a = [int(x) for x in input().strip().split()] # list of inputs
        product = getMinMax(a, n)
        print(product[0], end=" ") # Min element
        print(product[1])   # Max element
        T -= 1

if __name__ == "__main__":
    main()
