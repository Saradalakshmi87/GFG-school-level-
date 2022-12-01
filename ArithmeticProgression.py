#Finding Nth in the Arithmetic Progression 

def ArithmeticProgression(A1, A2, N):
    diff = A2 - A1
    return A1 + (N - 1)*diff

A1 = int(input())
A2 = int(input())
N = int(input())
print(A1, A2, N)