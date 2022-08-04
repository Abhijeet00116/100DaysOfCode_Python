def smallest(arr,size):
    minimum = arr[0]
    for i in range(0,size):
        if arr[i]<minimum:
            minimum = arr[i]
    return minimum

if __name__=='__main__':
    arr = [18,14,15,16,17,18,91,12,10]
    size = len(arr)
    print("Smallest element in array is -:",smallest(arr,size))