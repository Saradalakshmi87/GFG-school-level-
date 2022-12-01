'''
Given a number N. Count the number of digits in N which evenly divides N.

Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.

'''


class Solution:
    def evenlyDivides(self, N):
        c = 0
        t = N
        while N != 0:
            rem = N % 10
            if((rem != 0) and (t % rem == 0)):
                c += 1
            N //= 10
        return c

ob = Solution()
N = int(input())
print(ob.evenlyDivides(N))