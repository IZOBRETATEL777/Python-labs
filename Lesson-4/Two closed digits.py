# 'Да.' if contains two or more equal digits next to each other otherwise 'Нет.'
n = int(input('Введите натуральное число:\n'))
t = -1
while n > 0:
    if t == n % 10:
        print('Да.')
        break
    t = n % 10
    n //= 10
if n == 0:
    print('Нет.')
