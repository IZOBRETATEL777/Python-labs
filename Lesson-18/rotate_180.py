def printMatrix(a):
    for i in a:
        for j in i:
            print(f'{j:3d}', end=' ')
        print()
    print()


n = int(input("Enter N: "))
m = int(input("Enter M: "))
cur = 1
a = []
for i in range(n):
    a.append([0] * m)
    for j in range(m):
        a[i][j] = cur
        cur += 1
printMatrix(a)
for i in range(n // 2):
    a[i], a[-i - 1] = a[-i - 1], a[i]
print('Rotated 180')
printMatrix(a)