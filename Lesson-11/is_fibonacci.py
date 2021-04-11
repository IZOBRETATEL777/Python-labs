from random import randint


def isFibonacci(n):
    cur = 1
    last = 0
    while cur < n:
        t = cur
        cur += last
        last = t
    return n == cur


n = int(input('Введите длину массива: '))
a = [randint(-100, 100) for _ in range(n)]
print('Массив А:')
print(*a, sep=' ')
b = [i for i in a if isFibonacci(i)]
print('Массив B:')
if len(b) == 0:
    print('пуст :(')
else:
    
    print(*b, sep=' ')


