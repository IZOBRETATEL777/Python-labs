from random import randint


n = int(input('Введите длину массива: '))
a = [randint(-100, 100) for _ in range(n)]
print('Массив:')
print(*a, sep=' ')
used = [False for _ in range(n)]
atLeastOnce = False
for i in range(0, n):
    for j in range(0, i):
        if a[i] == a[j]:
            if used[j]:
                break
            else:
                atLeastOnce = True
                used[j] = True
                print(a[j], end=' ')
if atLeastOnce:
    print()
else:
    print('Нет')


