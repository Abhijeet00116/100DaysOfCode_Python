def commonElements (A, B, C, n1, n2, n3):
        # your code here
        val = []
        s1 = set()
        s2 = set()
        s3 = set()
        
        for i in A: 
            s1.add(i) 
        print(s1)

        for i in B: 
            s2.add(i)
        print(s2)

        for i in C:
            s3.add(i)
        print(s3)

        for num in A:
            if num in s1: 
                if num in s2: 
                    if num in s3:
                        if num not in val: val.append(num)
        return val
if __name__=="__main__":
    t = int(input())
    for tc in range (t):
        n1, n2, n3 = list(map(int,input().split()))
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        C = list(map(int,input().split()))

        res = commonElements(A, B, C, n1, n2, n3)
        if len (res) == 0:
            print (-1)
        else:
            for i in range (len (res)):
                print (res[i], end=" ")
            print ()