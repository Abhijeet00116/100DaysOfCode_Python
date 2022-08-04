import math
def secondSmallest(arr,size):
    smallest = second_smallest = math.inf # INT_MAx = math.inf

    for i in range(0,size):
        if arr[i]<smallest:
            second_smallest = smallest
            smallest= arr[i]
        elif arr[i]<second_smallest and arr[i]!= smallest:
            second_smallest = arr[i]

    return second_smallest

def smallest(arr,size):
    minimum = arr[0]
    for i in range(0,size):
        if arr[i]<minimum:
            minimum = arr[i]
    return minimum

if __name__=='__main__':
    arr = [18,14,15,16,17,18,91,12,10]
    size = len(arr)
    print("Second smallest element in array is -:",smallest(arr,size))
    print("Second smallest element in array is -:",secondSmallest(arr,size))