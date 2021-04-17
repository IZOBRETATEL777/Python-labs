from random import randint


def sumOfDigits(n):
    n = abs(n)
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s


def qSort(a, s, f, rev=False):
    if s >= f:
        return
    m = sumOfDigits(a[s + (f - s) // 2]) * (-1) ** rev
    l = s
    r = f
    while l <= r:
        while sumOfDigits(a[l]) * (-1) ** rev < m: l += 1
        while sumOfDigits(a[r]) * (-1) ** rev > m: r -= 1
        if l <= r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
    qSort(a, s, r, rev)
    qSort(a, l, f, rev)


n = 10
a = [randint(1, 1000) for _ in range(n)]
b = a[:]
print('Array:')
print(*a)
print('\nSorted with manually written Quick Sort:')
qSort(a, 0, n // 2 - 1)
qSort(a, n // 2, n - 1, rev=True)
print(*a)
print('\nSorted with standard sort:')
b = sorted(b[:n // 2], key=sumOfDigits) + sorted(b[n // 2:], key=sumOfDigits, reverse=True)
print(*b)
