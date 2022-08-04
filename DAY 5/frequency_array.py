def findFrequency (arr, n, x):
    c=0
    for i in range(n):
        if arr[i]==x:
            c+=1
    return c


if __name__=="__main__":
        
    t = int (input ()) #Total test Cases
    for tc in range (t):
        n = int (input ())# No of test cases inside a Test case
        arr = list (map (int, input ().split ())) # list of inputs
        x = int (input ()) # element to find frequency
        print (findFrequency (arr, n, x)) # frequency of the given "x" element