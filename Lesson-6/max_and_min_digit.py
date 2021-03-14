def extr_digits(n):
    n = abs(n)
    if n == 0:
        return 0, 0
    mx = -1
    mn = 10
    while n > 0:
        mx = max(mx, n % 10)
        mn = min(mn, n % 10)
        n //= 10
    return mx, mn


n = int(input('Enter an integer: '))
mx, mn = extr_digits(n)
print(f'Max digit is {mx}\nMin digit is {mn}')
