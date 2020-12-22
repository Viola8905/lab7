import random
import math
n=int(input("n"))
d=0
a = [[random.randint(0, 0) for j in range(n)] for i in range(n)]

for i in range (1,n):
    for j in range (1,n):
        if (i+j)%2==0:
            a[i][j]+=i
      
        else:
            a[i][j]+=j**2
print(a)
c=[]
b = []

b=[i*i for i in range(1,n)]
       
for i in list(b):
    if i>0:
        c.append(i)

    
print(max(c))
