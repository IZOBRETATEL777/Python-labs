from random import randint


def remExtr(a, n):
    max1 = a.index(max(a))
    min1 = a.index(min(a))
    b = []
    for i in range(n):
        if i != max1 and i != min1:
            b.append(a[i])
    max2 = b.index(max(b))
    min2 = b.index(min(b))
    print(f'Первый максимальный {a[max1]}, второй максимальный {b[max2]}')
    print(f'Первый минимальный {a[min1]}, второй минимальный {b[min2]}')
    a = []
    for i in range(n - 2):
        if i != max2 and i != min2:
            a.append(b[i])
    return a


n = 20
a = [randint(1, 100) for _ in range(n)]
print('Массив:', end=' ')
print(*a, sep=', ')
ans = remExtr(a, n)
print(*ans, sep=', ')

