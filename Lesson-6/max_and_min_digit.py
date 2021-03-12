def extr_digits(n):
    mx = -1
    mn = 10
    while n > 0:
        mx = max(mx, n % 10)
        mn = min(mn, n % 10)
        n //= 10
    return mx, mn


n = int(input())
mx, mn = extr_digits(n)
print(mx, mn)
