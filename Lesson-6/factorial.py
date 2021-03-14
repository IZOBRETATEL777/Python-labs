def my_factorial(n):
    res = 1
    for i in range (2, n + 1):
        res *= i
    return res


while True:
    n = int(input('Enter a natural number '))
    if n > 0:
        print('The factorial of the given number is:\n', my_factorial(n), sep='')
        break
    else:
        print('Try again')
