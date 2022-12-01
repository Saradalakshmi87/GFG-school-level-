class Solution:
    def diagonalSumDifference(self, N, Grid):
        #code here
        s1, s2 = 0, 0
        for i in range(N):
            s1 += Grid[i][i]
            s2 += Grid[N-i-1][i]
        return abs(s1-s2)
t = int(input())
for i in range(t):
    n = int(input())
    Grid = [[0 for _ in range(n)] for j in range(n)]
    for i in range(n):
        s = list(map(int, input().split()))
        for j in range(n):
            Grid[i][j] = s[j]
    ob = Solution()
    print(ob.diagonalSumDifference(n, Grid))