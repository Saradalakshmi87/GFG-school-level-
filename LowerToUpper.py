'''
Given a string str containing only lowercase letters, generate a string with the same letters, but in uppercase.
'''


class Solution:
    def to_upper(self, str):
        # code here
        s = ""
        for i in str:
            s += chr(ord(i) & (~(1 << 5)))
        return s
ob = Solution()
s = input()
print(ob.to_upper(s))