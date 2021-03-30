from random import randint


n = int(input('Введите длину массива. ОСТОРОЖНО! При больших значениях элементов массива программа может не работать!\n'))
a = [randint(-100, 100) for _ in range(n)]
print('Массив:')
print(*a, sep=' ')
atLeastOnce = False
l = min(a)
r = max(a)
for cur in range(l, r + 1):
    seen = 0
    for i in a:
        if i == cur:
            seen += 1
        if seen > 1:
            if not atLeastOnce:
                print('Есть:', end=' ')
                atLeastOnce = True
            print(cur, end=' ')
            break
if atLeastOnce:
    print()
else:
    print('Нет') 
