'''
Given a number, reverse it and add it to itself unless it becomes a palindrome or number of iterations becomes more than 5.

Example 1:
----------
Input: n = 23
Output: 55 

Explanation: 
............
reverse(23) = 32,then 32+23
= 55 which is a palindrome. 

'''
def rev(val):
    rev = 0
    while val != 0:
        rev = (rev*10) + (val%10)
        val //= 10
    return rev
def isSumPalindrome(n):
    t = n
    for i in range(6):
        if t == rev(t):
            return t
        else:
            t += rev(t)
    return -1

n = int(input())
print(isSumPalindrome(n))