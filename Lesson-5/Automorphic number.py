import math

while True:
    n = int(input('Enter natural number: '))
    if n < 0:
        print('Error, try again')
    else:
        break
flag = False
for i in range(1, n + 1):
    if i == 0:
        l = 0
    else:
        l = math.floor(math.log10(i)) + 1
    t = i * i
    if t % 10 ** l == i:
        if not flag:
            print(f'Automorphic numbers from 1 to {n} are:')
        print(f'{i}*{i}={i * i}')
        flag = True
