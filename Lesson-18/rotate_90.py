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
b = []
for j in range(m):
    t = []
    for i in range(n - 1, -1, -1):
        t.append(a[i][j])
    b.append(t)
print('Rotated 90:')
printMatrix(b)