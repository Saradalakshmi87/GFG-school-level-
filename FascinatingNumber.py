'''
Given a number N. Your task is to check whether it is fascinating or not.
Fascinating Number: When a number(should contain 3 digits or more) is multiplied by 2 and 3 ,and when both these products are concatenated with the original number, then it results in all digits from 1 to 9 present exactly once.

Example 1:

Input: 
N = 192

Output: Fascinating
Explanation: After multiplication with 2
and 3, and concatenating with original
number, number will become 192384576 
which contains all digits from 1 to 9.

'''

def fascinating(n):
    s = 0
    two = str(n*2)
    three = str(n*3)
    res = int(str(n)+two+three)
    while(res != 0):
        s += (res % 10)
        res //= 10
    if s == 45:
        return "Fascinating"
    else:
        return "Not Fascinating"

n = int(input())
print(fascinating(n))
