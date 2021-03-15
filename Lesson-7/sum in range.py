def sumAb(a, b):
    s = 0
    for i in range(a, b + 1):
        s += i
    return s
a, b = map(int, input('Enter range (two natural numbers): ').split())
print(sumAb(a, b))
