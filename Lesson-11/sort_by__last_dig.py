n = int(input())
a = [int(i) for i in input().split()]
for i in range(0, n - 1):
    for j in range(0, n - i - 1):
        if a[j] % 10 > a[j + 1] % 10:
            a[j], a[j + 1] = a[j + 1], a[j]
print(*a, sep=' ')

