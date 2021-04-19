n = int(input())
a = [int(x) for x in input().split()]
x = int(input())

l = 0
r = n
while r - l > 0:
    m = l + (r - l) // 2
    if x > a[m]:
        l = m + 1
    else:
        r = m
lb = l
l = 0
r = n
while r - l > 0:
    m = l + (r - l) // 2
    if x >= a[m]:
        l = m + 1
    else:
        r = m
ub = l
print(lb, ub, ub - lb)

