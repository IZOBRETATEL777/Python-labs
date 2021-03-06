a, b = map(abs, map(int, input('Enter two integers in one line:\n').split()))
a1, b1 = a, b
while a > 0 and b > 0:
    if a > b:
        a %= b
    else:
        b %= a
print(f'GCD({a1},{b1})={a + b}')

