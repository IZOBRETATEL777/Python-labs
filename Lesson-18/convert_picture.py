from random import randint


def printMatrix(a):
    for i in a:
        for j in i:
            print(f'{j:4d}', end=' ')
        print()
    print()


def avg(a):
    return sum(a) / len(a)


n = 7
a = [list(randint(0, 255) for _ in range(n)) for _ in range(n)]
printMatrix(a)
avgBrig = avg([avg(i) for i in a])
for i in range(len(a)):
    for j in range(len(a[i])):
            a[i][j] = 255 * (avgBrig > a[i][j])
printMatrix(a)
print(*a)
