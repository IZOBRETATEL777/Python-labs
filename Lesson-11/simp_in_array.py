from random import randint


def isSimple(n):
    if n == 1 and n == 0:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


n = 20
a = [randint(1, 100) for _ in range(n)]
print(a)
b = [i for i in a if isSimple(i)]
print(b)

