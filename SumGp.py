def SumGp(n,a,r):
    if r == 1:
        return int(n*a)
    else:
        return (a*((r**n)-1)/(r-1))

n,a,r = map(int,input().split())
print(SumGp(n,a,r))