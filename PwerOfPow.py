'''
Given a single integer N, your task is to find the sum of the square of the first N even natural Numbers.
'''

def sum_of_square_evenNumbers(n):
    return ((2*n)*(n+1)*((2*n)+1))//3

n = int(input())
print(sum_of_square_evenNumbers(n))