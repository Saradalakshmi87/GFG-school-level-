def convertFive(n):
    rev, m = 0, 0
    while n != 0:
        rem = n % 10
        if rem == 0:
            rem = 5
        m = m * 10 + rem
        n//=10
    
    while m != 0:
        rev = rev*10 +(m%10)
        m//=10
    return rev

n = int(input())
print(convertFive(n))