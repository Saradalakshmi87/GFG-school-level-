'''
Given a string S, write a program to count the occurrence of Lowercase characters, Uppercase characters, Special characters and Numeric values in the string.
Note: There are no white spaces in the string.
'''


class Solution:
    def count(self, s):
        # your code here
        l = [0, 0, 0, 0]
        for i in s:
            if i.isupper():
                l[0] += 1
            elif i.islower():
                l[1] += 1
            elif i.isdigit():
                l[2] += 1
            else:
                l[3] += 1
        return l
ob = Solution()
s = input()
print(ob.count(s))