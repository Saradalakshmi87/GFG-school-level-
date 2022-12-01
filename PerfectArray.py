'''
Given an array of size N and you have to tell whether the array is perfect or not. An array is said to be perfect if it's reverse array matches the original array. If the array is perfect then print "PERFECT" else print "NOT PERFECT".
'''
class Solution:
    def IsPerfectArray(self,arr,n):
        i, j = 0, n-1
        while i <= j:
            if arr[i] != arr[j]:
                return False
        return True

for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    if ob.IsPerfectArray(arr,n):
        print("PERFECT")
    else:
        print("NOT PERFECT")
