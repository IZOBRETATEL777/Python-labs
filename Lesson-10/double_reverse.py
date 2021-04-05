from random import randint
n = 20
a = [randint(1, 200) for _ in range(n)]
print('Массив:')
print(*a, sep=', ')
print('Перевернутый:')
m = n // 2
for i in range(0, m // 2):
    a[i], a[m - i - 1] = a[m - i - 1], a[i]
for i in range(m, m + m // 2):
    a[i], a[n - i - 1 + m] = a[n - i - 1 + m], a[i]
print(*a, sep=', ')
