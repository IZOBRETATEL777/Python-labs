def isFibonacci(n):
    cur = 1
    last = 0
    while cur < n:
        t = cur
        cur += last
        last = t
    return n == cur
n = int(input())
a = [int(i) for i in input().split()]
b = [i for i in a if isFibonacci(i)]
if len(b) == 0:
    print('0')
else:
    print(*b, sep=' ')


