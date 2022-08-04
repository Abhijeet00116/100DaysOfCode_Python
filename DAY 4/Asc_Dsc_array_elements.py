def asc_dsc(arr, n):
    arr.sort()
    for i in range(n // 2):
        print(arr[i], end = " ")    # 1st half

    for j in range(n - 1, n // 2 -1, -1):
        print(arr[j], end = " ")    # 2nd half

if __name__ == '__main__':
        
    arr = [ 5, 4, 6, 2, 1, 3, 8, 0]
    n = len(arr)
    print("Original Array -: ",arr)

    print("Ascending Descending Array -: ",end=" ")

    asc_dsc(arr, n)