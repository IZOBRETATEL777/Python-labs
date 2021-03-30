from random import randint


n = int(input('Введите длину массива. ОСТОРОЖНО! При больших значения элементов массива программа может не работать!\n'))
a = [randint(-100, 100) for _ in range(n)]
print('Массив:')
print(*a, sep=' ')
delta = abs(min(a))
sz = max(a) + delta + 1
cnt = [0 for _ in range(sz)]
for i in a:
    cnt[i + delta] += 1
atLeastOnce = False
for i in range(sz):
    if cnt[i] > 1:
        if not atLeastOnce:
            print('Есть:', end=' ')
        atLeastOnce = True
        print(i - delta, end=' ')
if atLeastOnce:
    print()
else:
    print('Нет')

