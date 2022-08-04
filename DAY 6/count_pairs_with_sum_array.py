def pairCount_1(List,n,k):
    flag = False
    c=0
    for i in range(n):
        for j in range(i+1,n):
            if List[i]+List[j] == k:
                c = c+1
                flag = True
    return c

def pairCount_2(List,n,k):
    d={} # distionary
    count=0
    for i in List:
        ans=k-i
        if ans in d:
            count+=d[ans]
        if i in d:  
            d[i]+=1
        else:   
            d[i]=1
    return count

if __name__ == '__main__':
    testCase = int(input())
    while testCase > 0:
        n,k = list(map(int,input().split()))
        List = list(map(int,input().split()))
        print(pairCount_2(List,n,k))

        print(pairCount_1(List,n,k))
        
        testCase = testCase -1
