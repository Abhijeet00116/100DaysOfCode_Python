def sortArr(arr, n): 
        #code here
        arr.sort()
        return arr

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ans = sortArr(arr, n)
        for i in ans:
            print(i,end=" ")
        print()