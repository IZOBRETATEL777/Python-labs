# find all prime divisors of a number
def getPrimeDivisors(n : int) -> list:
    i = 2
    divs = [1]
    while i * i <= n:
        if n % i == 0:
            divs.append(i)
        while n % i == 0:
            n //= i
        i += 1
    if n > 1:
        divs.append(n)
    return divs


# check whether it is powerefull
def isPowerfullNumber(n):
    res = True
    for i in getPrimeDivisors(n):
        res = res and n % (i * i) == 0
    return res


# main program
n = int(input())
if isPowerfullNumber(n):
    print('The given number is powerfull')
else:
    print('The given number is not powerfull')

