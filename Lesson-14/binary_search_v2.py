def binary_search(a, x):
    l = -1
    r = len(a)
    while r - l > 1:
        m = l + (r - l) // 2
        if a[m] < x:
            l = m
        else:
            r = m
    return (r < n and a[r] == x)


n, m = map(int, input().split())
a = [int(x) for x in input().split()]
queries = [int(x) for x in input().split()]
for q in queries:
    if binary_search(a, q):
        print('YES')
    else:
        print('NO')
