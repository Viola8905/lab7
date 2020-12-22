r = int(input("Введіть кількість рядків та стовпців матриці: "))

a = [[float(input("Введіть координати матриці a[{0}][{1}]=".format(i,j))) for j in range(r)] for i in range(r)]

print(a)

for i in range(r):
        if i % 2 == 0:
            a[i].sort(reverse=True)


print("Відсортована матриця: {0}".format(a))

            
