from math import sqrt
a, b, c = map(int, input('Enter a, b and c: ').split())
if a == b == c == 0:
    print('No solution. Equation is not correct!')
elif a == 0:
    print(f'Not a quadratic equation. It is linear one\nAnswer is {c / b:.2f}')
else:
    # using discriminant formula
    d = b ** 2 - 4 * a * c
    if d < 0:
        print('No real roots')
    elif d == 0:
        x = (-b - sqrt(d)) / (2 * a)
        print(f'{x:0.2f} is only root of the given equation')
    else:
        x1 = (-b - sqrt(d)) / (2 * a)
        x2 = (-b + sqrt(d)) / (2 * a)
        print(f'{x1:0.2f} and {x2:0.2f} are roots of the given equation')
