from random import randint


#n = 20
n = int(input('Введите длину массива: '))
a = [randint(-100, 100) for _ in range(n)]
print('Массив:')
print(*a, sep=' ')
#bubble sort implementation
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if a[j + 1] <= 0 and a[j] >= 0:
            a[j], a[j + 1] = a[j + 1], a[j]
print(*a, sep=' ')

