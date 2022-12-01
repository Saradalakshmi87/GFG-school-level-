def ArraySum(arr, n):
    res = 0
    for i in arr:
        res += i
    return res

size = int(input())
arr = [i for i in input().split()]
print(ArraySum(arr, size))