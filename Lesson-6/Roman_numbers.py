def to_roman(n):
    while n >= 1000:
        n -= 1000
        print('M', end='')
    while n >= 900:
        n -= 900
        print('CM', end='')
    while n >= 500:
        n -= 500
        print('D', end='')
    while n >= 400:
        n -= 400
        print('CD', end='')
    while n >= 100:
        n -= 100
        print('C', end='')
    while n >= 90:
        n -= 90
        print('XC', end='')
    while n >= 50:
        n -= 50
        print('L', end='')
    while n >= 40:
        n -= 40
        print('XL', end='')
    while n >= 10:
        n -= 10
        print('X', end='')
    while n >= 9:
        n -= 9
        print('IX', end='')
    while n >= 5:
        n -= 5
        print('V', end='')
    while n >= 4:
        n -= 4
        print('IV', end='')
    while n >= 1:
        n -= 1
        print('I', end='')
    print()



n = int(input())
to_roman(n)
