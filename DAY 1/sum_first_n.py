def normal_sum(i,n):
    for i in range(i,n):
        Sum += i
    return Sum

def recursive_sum(i,Sum):
    if i<1:
        return Sum
    recursive_sum(i-1,Sum+i)

if __name__=='__main__':
    n = int(input('N ->'))
    
    print("Sum of "+str(n)+" numbers -: ")
    recursive_sum(n,0)
    normal_sum(0,n)
