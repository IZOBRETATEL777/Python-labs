from random import randint


def rem(a, n, idx):
    for i in range(idx, n - 1):
        a[i] = a[i + 1]
    print(a)
    return a, n - 1


n = 20
a = [randint(1, 100) for _ in range(n)]
print(a)
i = 0
while i < n:
    if a[i] <= 15:
        a, n = rem(a, n, i)
        i = i - 1
    else:
        i += 1
for i in range(0, n):
    print(a[i], end=' ')

