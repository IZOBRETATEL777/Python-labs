from random import randint


def remExtr(a, n):
    toDel = [a[0]] * 4
    for i in a:
        if i > toDel[0]:
            toDel[1] = toDel[0]
            toDel[0] = i
        else:
            toDel[1] = max(toDel[1], i)
        if i < toDel[2]:
            toDel[3] = toDel[2]
            toDel[2] = i
        else:
            toDel[3] = min(toDel[3], i)
    print(f'Первый максимальный {toDel[0]}, второй максимальный {toDel[1]}')
    print(f'Первый минимальный {toDel[2]}, второй минимальный {toDel[3]}')
    idx = []
    for i in range(4):
        for j in range(n):
            if a[j] == toDel[i] and j not in idx:
                idx.append(j)
                break
    b = []
    for i in range(n):
        if i not in idx:
            b.append(a[i])
    return b


n = 20
a = [randint(1, 100) for _ in range(n)]
print('Массив:', end=' ')
print(*a, sep=', ')
ans = remExtr(a, n)
print(*ans, sep=', ')

