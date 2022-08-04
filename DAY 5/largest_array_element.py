def largest(arr,size):
    maximum = arr[0]
    for i in range(0,size):
        if arr[i]>maximum:
            maximum = arr[i]
    return maximum

if __name__=='__main__':
    arr = [18,14,15,16,17,28,12,10]
    size = len(arr)
    print("Smallest element in array is -:",largest(arr,size))