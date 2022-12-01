'''
In a party of N people, each person is denoted by an integer. Couples are represented by the same number. Find out the only single person in the party of couples.


Example 1:

Input: N = 5
arr = {1, 2, 3, 2, 1}
Output: 3
Explaination: Only the number 3 is single.

'''
N = int(input())
arr = [int(i) for i in input().split()]
res = 0
for i in arr:
    res ^= i
print(res)