from math import log10
from math import floor


def swapDigs(n):
    if n == 0:
        l = 1
    else:
        l = floor(log10(n)) + 1
    d1 = n // 10 ** (l - 1)
    d2 = n % 10
    n1 = (d2 * (10 ** (l - 1)) + n % (10 ** (l  - 1))) // 10 * 10 + d1
    return n1


n = int(input())
print(swapDigs(n))
