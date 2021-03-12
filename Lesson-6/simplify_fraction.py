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


a, b = map(int, input().split())
a, b = simplify(a, b)
print(a, b)
