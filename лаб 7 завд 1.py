import random
#Визначити суму від’ємних елементів матриці з парною сумою індексів.

r=int(input("кількість рядків r="))
e=int(input("кількість елементів e="))

a=[[random.randint(-10,20)  for j in range(e)] for i in range(r)]

b=[]
for row in a:
    row_str=['{0:5d}'.format(el) for el in row]
    b.append(row_str)

b=[''.join([ '{0:7d}'.format(el) for el in row])   for row in a]
print(*b,sep='\n')

s=0
for i in range(r):
    for j in range(e):
        if a[i][j]<0 and (i+j)%2==0:
            s+=a[i][j]
print(s)
