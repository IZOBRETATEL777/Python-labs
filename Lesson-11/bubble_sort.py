a = [1, 3, 2, 9, 4, 1]
n = len(a)
for i in range(0, n - 1):
    for j in range(n - 2, 0 + i, -1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(a)
