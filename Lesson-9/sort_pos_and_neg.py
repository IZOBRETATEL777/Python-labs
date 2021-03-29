n = int(input())
a = [int(x) for x in input().split()]
#bubble sort implementation
for i in range(n - 1):
    for j in range(0, n - i - 1):
        if a[j] <= 0 and a[j + 1] >= 0:
            a[j], a[j + 1] = a[j + 1], a[j]
print(*a, sep=' ')

