from math import cos, pi


def solve(x):
    r = 0
    n = 1
    while True:
        t = (x ** n *  cos(n * pi / 3)) / n
        if abs(t) < 1e-8:
            break
        r += t
        n += 1
    return r


x = 0.1
while x <= 0.8:
    print(f'f({x:g})={solve(x)}')
    x += 0.1


