def GCD(a, b):
    a, b = abs(a), abs(b)
    while a > 0 and b > 0:
        if a > b:
            a %= b
        else:
            b %= a
    return a + b


def LCM(a, b):
    a, b = abs(a), abs(b)
    return a // GCD(a, b) * b


a, b = map(int, input().split())
print(LCM(a, b), GCD(a, b))

