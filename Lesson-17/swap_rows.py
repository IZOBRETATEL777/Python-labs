from random import randint

n = 5
m = 4
a = [list(randint(10, 90) for _ in range(m)) for _ in range(n)]
print('Matrix:')
for i in a:
    for j in i:
        print(j, end=' ')
    print()
print()
print('The first and the last rows has been swapped!')
for i in range(m):
    a[0][i], a[n - 1][i] = a[n - 1][i], a[0][i]
for i in a:
    for j in i:
        print(j, end=' ')
    print()


