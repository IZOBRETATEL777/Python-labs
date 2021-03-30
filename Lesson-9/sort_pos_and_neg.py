from random import randint


n = 20
a = [randint(-100, 100) for _ in range(n)]
print('Массив:')
print(*a, sep=' ')
neg = []
zero = 0
pos = []
for i in a:
    if i < 0:
        neg.append(i)
    if i == 0:
        zero += 1
    if i > 0:
        pos.append(i)
print(*neg, *([0] * zero), *pos, sep=' ')

