'''Given an array Arr of size N, print second largest element from an array.'''

def SecondLargest(arr):
    first = second = -2147483648
    arr_size = len(arr)
    if arr_size < 2:
        return -1
    
    for i in range(arr_size):
        if arr[i] > first:
            second = first
            first = arr[i]
        elif (arr[i] > second) and (arr[i]!=first):
            second = arr[i]
    
    if second != -2147483648:
        return second
    return -1



arr = [int(i) for i in input().split()]
print(SecondLargest(arr))
