def GCD(a, b):
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def LCM(a, b):
    return a // GCD(a, b) * b

while True:
    a, b = map(int, input('Enter two natural numbers in one line: ').split())
    if a <= 0 or b <= 0:
        print('Wrong numbers! Try again')
    else:
        print(f'GCD({a},{b})={GCD(a, b)}')
        print(f'LCM({a},{b})={LCM(a, b)}')
        break

