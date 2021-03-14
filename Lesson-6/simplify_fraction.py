def GCD(a, b):
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def simplify(a, b):
    if b == 0:
        return a, b
    d = GCD(abs(a), abs(b))
    if a < 0 and b < 0: 
        d *= -1
    return a // d, b // d


a, b = map(int, input('Enter the numerator and denumerator of a fraction in one line:\n').split())
if a == 0:
    print('Answer is 0/1 or 0. Are you not mistaken?')
elif b == 0:
    print('It is impossible to devide by 0!')
else:
    a, b = simplify(a, b)
    print(f'Simplified fraction: {a}/{b}')

