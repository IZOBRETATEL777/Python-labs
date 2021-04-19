def lower_bound(a, x):
    l = -1
    r = len(a)
    while r - l > 1:
        m = l + (r - l) // 2
        if a[m] < x:
            l = m
        else:
            r = m
    return r


n, m = map(int, input().split())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
for i in b:
    ub = lower_bound(a, i)
    if ub == n:
        ub -= 1
    lb = max(ub - 1, 0)
    if a[lb] == i:
        print(i)
    else:
        if abs(a[lb] - i) <= abs(a[ub] - i):
            print(a[lb])
        else:
            print(a[ub])

