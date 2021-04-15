def qSort(a, s, f):
    if s >= f:
        return
    m = a[s + (f - s) // 2]
    l = s
    r = f
    while l <= r:
        while a[l] < m: l += 1
        while a[r] > m: r -= 1
        if l <= r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1


n = int(input())
a = [int(i) for i in input().split()]
qSort(a, 0, n - 1)
ans = 1
for i in range(0, n - 1):
    if a[i] != a[i + 1]:
        ans += 1
print(ans)


