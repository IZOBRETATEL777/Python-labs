n = int(input('Введите число элементов: '))
print('Введите элементы массива (каждый в на новой строке):')
a = [0] * n
a[0] = int(input())
m = a[0]
cnt = 1
for i in range(1, n):
    a[i] = int(input())
    if a[i] > m:
        cnt = 1
        m = a[i]
    elif a[i] == m:
        cnt += 1
print("Массив:", *a, sep=' ')
print('Максимальное значение:', m)
print('Количество элементов:', cnt)

