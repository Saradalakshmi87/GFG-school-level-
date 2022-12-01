'''
Given a stream of incoming numbers, find average or mean of the stream at every point.

Example 1:
-------------
Input:
.....
n = 5
arr[] = {10, 20, 30, 40, 50}

Output:
......
10.00 15.00 20.00 25.00 30.00 

Explanation: 
............
10 / 1 = 10.00
(10 + 20) / 2 = 15.00
(10 + 20 + 30) / 3 = 20.00
And so on.

'''

def Avg(arr):
    res = []
    cnt, s = 1, 0
    for i in arr:
        s += i
        val = s/cnt
        res.append(val)
        cnt += 1
    return res

arr = [int(i) for i in input().split()]
print(Avg(arr))