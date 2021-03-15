from math import sin
from math import pi


def myFactorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def mySin(x):
    sign = 1
    res = 0
    eps = 1e-15
    i = 1
    while True:
        cur = sign * (x ** i / myFactorial(i))
        if eps > abs(cur):
            break
        res += cur
        sign *= -1
        i += 2
    return res


def toRadian(x):
    return x / 180 * pi


a = toRadian(float(input('Enter an angle in degrees: ')))
print(f'Sin of {a:g} by MySin        {mySin(a)}')
print(f'Sin of {a:g} by std function {sin(a)}')
