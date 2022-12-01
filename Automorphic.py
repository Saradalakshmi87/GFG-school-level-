class Solution:
    def is_Automorphic(self, n):
        sq = n*n
        while n:
            if n%10 != sq%10:
                return "Not Automorphic"
            n //= 10
            sq //= 10
        return "Automorphic"

n = int(input())
ob = Solution()
print(ob.is_Automorphic(n))