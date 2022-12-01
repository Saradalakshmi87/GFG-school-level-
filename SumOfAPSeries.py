'''
A series with same common difference is known as arithmetic series. The first term of series is 'a' and common difference is d. The series looks like a, a + d, a + 2d, a + 3d, . . . Find the sum of series upto nth term.
'''
def SeriesSum(n, a, d):
    return n*(2*a + (n-1)*d)//2

n, a, d = map(int,input().split())
print(SeriesSum(n,a,d))