a = [6, 34, 44, 44, 44, 55, 67, 78, 82]
n = len(a)
x = 44

l = 0
r = n
while r - l > 1:
    m = l + (r - l) // 2
    if x >= a[m]:
        l = m;
    else:
        r = m;
print(f'a[{l}]={x}')
