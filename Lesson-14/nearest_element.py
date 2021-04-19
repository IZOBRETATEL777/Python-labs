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
dif = abs(a[0] - a[-1])
ans = -1
if lb != ub:
    ans = a[lb]
    dif = 0
else:
    if lb > 0:
        al = a[lb - 1]
        if abs(al - x) <= dif:
            dif = abs(al - x)
            ans = al
    if ub < n:
        ar = a[ub]
        if abs(ar - x) <= dif:
            dif = abs(ar - x)
            ans = ar
print(ans, dif)
    
    
