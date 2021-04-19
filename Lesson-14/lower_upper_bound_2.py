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


def upper_bound(a, x):
    l = -1
    r = len(a)
    while r - l > 1:
        m = l + (r - l) // 2
        if a[m] <= x:
            l = m
        else:
            r = m
    return r


n, m = map(int, input().split())
a = [int(x) for x in input().split()]
for i in b:
lb = lower_bound(a, m)
ub = upper_bound(a, m)
print(lb, ub)


