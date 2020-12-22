import random
n=int(input("кількість рядків ="))

a=[[random.randint(-10,10)  for j in range(n)] for i in range(n)]
c=[]
b=[]

for j in range (n):
    for i in range (n):
        if a[i][j]>0:
            b.append(a[i][j])
            
c=sum(b)
print(c)
print(b)
print(a)
