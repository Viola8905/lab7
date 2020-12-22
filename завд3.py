import math
import random
r=int(input("кількість рядків r="))
e=int(input("кількість стовпців e="))
n=int(input("n="))

x = [float(input("Веідть {0}-у координату вектора: ".format(i+1))) for i in range(n)]
print("Вектор х={0}".format(x))

b=0

for el in range (1):
    b+=(math.sqrt((x[0]**2)+(x[1]**2)))
print(b)

a=[[random.randint(-10,20)  for j in range(e)] for i in range(r)]
print("Матриця А={0}".format(a))


c= [[a[i][j]*b for j in range(e)] for i in range(r)]
print("добуток матриці на вектор={0}".format(c))


