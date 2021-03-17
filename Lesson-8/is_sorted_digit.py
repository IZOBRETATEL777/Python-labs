def isSorted(n):
    n = abs(n)
    res = True
    last = n % 10
    while n > 0:
        res &= (n % 10 <= last)
        last = n % 10
        n //= 10
    return res


n = int(input())
if isSorted(n):
    print('YES')
else:
    print('NO')

