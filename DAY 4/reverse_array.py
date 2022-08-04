def reverseList(A, start, end):
      while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1

if __name__=='__main__':
        
    A = [10, 20, 30, 40, 50]
    print("Array before Reverse -: ",A)
    reverseList(A, 0, 4)
    print("Array After Reverse -: ",A)