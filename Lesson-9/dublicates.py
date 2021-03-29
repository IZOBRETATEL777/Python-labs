n = int(input())
a = list(map(int, input().split()))
rep = []
for i in range(0, n - 1):
    for j in range(i + 1, n):
        if a[i] == a[j] and a[i] not in rep:
            rep += [a[i]]
if len(rep) == 0:
    print('0')
else:
    print(*rep, sep=' ')


