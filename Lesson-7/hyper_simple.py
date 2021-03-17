def isSimple(n):
    if n == 1:#1 is not a simnple number
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def isHyperSimple(n):
    n = abs(n)
    res = True
    while n > 0:
        res &= isSimple(n)
        n //= 10
    return res


n = int(input('Enter an integer: '))
if (isHyperSimple(n)):
    print('The given number is hypersimple')
else:
    print('The given number is not hypersimple')