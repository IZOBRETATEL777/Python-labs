while True:
    n = int(input('Enter natural number: '))
    if n <= 0:
        print('Error, try again')
    else:
        break
for i in range(1, n + 1):
    cur = i
    square = i * i
    while cur > 0:
        if cur % 10 != square % 10:
            break
        square //= 10
        cur //= 10
    if cur == 0:
        print(f'{i}*{i}={i * i}')
