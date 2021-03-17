from math import exp


def myFactorial(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


def myExponent(x):
    eps = 1e-15
    res = 1
    i = 1
    while True:
        cur = x ** i / myFactorial(i)
        if abs(cur) < eps:
            break
        res += cur
        i += 1
    return res


print(' e^x \t MyExponent(x)\t\t Math.exp(x)')
for i in range(-10, 11):
    print(f'e^({i:3d}) | {myExponent(i):21.15f} | {exp(i):21.15f}')
