class Solution:
    def prime(self, n):
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    def fullPrime(self, N):
        #code here
        f = False
        t = N
        if self.prime(t):
            f = True
        else:
            return 0
        while N != 0:
            rem = N % 10
            if rem == 1 or rem == 0:
                return 0
            elif (self.prime(rem)):
                f = True
            else:
                return 0
            N //= 10
        if f:
            return 1
        else:
            return 0

ob = Solution()
n = int(input())
print(ob.fullPrime(n))