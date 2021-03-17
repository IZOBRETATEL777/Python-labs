def GCD(a, b):
    print(a, b)
    return a if b == 0 else GCD(b, b % a)

a, b = map(int, input().split())
print(GCD(a, b))
