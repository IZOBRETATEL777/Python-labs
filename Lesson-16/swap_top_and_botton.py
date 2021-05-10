from random import randint


n = 4
m = 5
a = [list(randint(10, 90) for j in range(m)) for i in range(n)]
for i in a:
    for j in i:
        print(f'{j:2d}', end=' ')
    print()
s = 0
for i in range(n):
    for j in range(i + 1):
        s += a[i][j]
print(s)

