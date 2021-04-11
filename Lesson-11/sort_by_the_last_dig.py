from random import randint


n = 20
a = [randint(1, 100) for _ in range(n)]
print('Array:')
print(*a, sep=' ')
print('Sorted by the last digit array:')
for i in range(0, n - 1):
    for j in range(0, n - i - 1):
        if a[j] % 10 > a[j + 1] % 10:
            a[j], a[j + 1] = a[j + 1], a[j]
print(*a, sep=' ')

