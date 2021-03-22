def numberOfTerms(n, reduction=1):
    if n == 0:
        return 1
    res = 0
    while reduction <= n:
        res += numberOfTerms(n - reduction, reduction)
        reduction += 1
    return res


while True:
    n = int(input('Enter a natural number: '))
    if n <= 0:
        print('Try again')
    else:
        break
print('The given number can be presented in', numberOfTerms(n) - 1, 'ways') #minus case where only one term n
