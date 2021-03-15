def isPalindorme(n):
    n = abs(n)
    rev = 0
    n1 = n
    while n > 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev == n1


n = int(input('Enter an integer: '))
if (isPalindorme(n)):
    print('It is a palindrome')
else:
    print('It is not a palindrome')