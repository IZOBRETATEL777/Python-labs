from random import randint


n = int(input('Введите длину массива: '))
a = [randint(-100, 100) for _ in range(n)]
print('Массив:')
print(*a, sep=' ')
rep = []
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if a[i] == a[j] and a[i] not in rep:
            rep += [a[i]]
if len(rep) == 0:
    print('Нет')
else:
    print('Есть:', *rep, sep=' ')


