from random import randint


def printMatrix(a):
    for i in a:
        for j in i:
            print(f'{j:2d}', end=' ')
        print()
    print()


n = 7
a = [list(randint(10, 90) for _ in range(n)) for _ in range(n)]
printMatrix(a)
for i in range(n):
    a[i][0] = 0
    a[i][-1] = 0
    a[i][n // 2] = 0
    a[-1][i] = 0
printMatrix(a)


