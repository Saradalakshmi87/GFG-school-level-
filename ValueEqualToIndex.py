'''
Input: 
------
N = 5
Arr[] = {15, 2, 45, 12, 7}

Output: 2

'''
def ValueEqualToIndex(arr, n):
    res = []

    if n == 0:
        return -1
    
    for i in range(1, n+1):
        if i == arr[i-1]:
            res.append(i)
    return res

n = int(input())
arr = [int(i) for i in input().split()]
print(ValueEqualToIndex(arr, n))


# If the given array is sorted, then we can use the binary search approach by keep on comparing the 'mid' and 'arr[i]' till we found the resultant value. Otherwise, return -1.