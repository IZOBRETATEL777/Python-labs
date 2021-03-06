from math import floor
from math import log10

n = abs(int(input('Enter integer: ')))
l = 0 if n == 0 else 1 + floor(log10(n))
lim = l // 2 + 1
flag = True

for i in range(1, lim):
    left = n % 10 ** i // 10 ** (i - 1)
    right = n // 10 ** (l - i) % 10
    if left != right:
        flag = False

if flag:
    print('It is a palindrome!')
else:
    print('It is not a palindrome')
