import math
n = int(input('n = '))
A = [[int(input('A[{0}][{1}] = '.format(i,j))) for j in range(n)]for i in range(n)]
print(A)


Summ = 0
B = []

for i in range(n):
    k = i
    l = 0
    for j in range(i+1):
        Summ += A[k][j]
        k -= 1
        l += 1
    B.append(math.fabs(Summ))
    Summ = 0
B.pop()

for i in range(n):
    k = n - 1
    l = i
    for j in range(n-i):
        Summ += A[k][l]
        l += 1
        k -= 1
    B.append(math.fabs(Summ))
B.pop(n-1)
print(B)
print(min(B))
