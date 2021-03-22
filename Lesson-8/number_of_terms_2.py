def rec(n, k):
    if n == 0 and k == 0:
        return 1
    if k == 0:
        return 0
    if n >= k:
        return rec(n, k - 1) + rec(n - k, k)
    else:
        return rec(n, n)


while True:
    n = int(input('Enter a natural number: '))
    if n <= 0:
        print('Try again')
    else:
        break
print('The given number can be presented in', rec(n, n) - 1, 'ways') #minus case where only one term n