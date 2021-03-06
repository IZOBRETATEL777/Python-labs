# 'Да.' if contains two equal digits otherwise 'Нет.'
n = int(input('Введите натуральное число:\n'))
n1 = n
digit = 0
flag = False
while digit < 10:
    n = n1
    cnt = 0  
    while n > 0:
        if n % 10 == digit:
            cnt += 1
        n //= 10
    if cnt >= 2:
        if flag == False:
            print('Да.')
        print('Число', digit, 'повторяется', cnt, 'раз')
        flag = True
    digit += 1
if flag == False:
    print('Нет.')
