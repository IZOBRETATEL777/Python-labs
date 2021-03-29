from random import randint


n = int(input('Введите длину массива: '))
a = [randint(0, 5) for _ in range(n)]
print('Массив:')
print(*a, sep=' ')
x = int(input('Что ищем:\n'))
flag = False
for i in range(0, n ):
    if a[i] == x:
        if not flag:
            print('Нашли:', end=' ')
        else:
            print(',', end=' ')
        flag = True
        print(f'A[{i}]={a[i]}', end='')
if flag:
    print()
else:
    print('Ничего не нашли.')
