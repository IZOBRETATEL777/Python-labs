def myFactorial(n):
    if n == 0:
        return 1
    return n * myFactorial(n - 1)


while True:
    n = int(input('Enter a postitive integer: '))
    if n < 0:
        print('Try again')
    else:
        break
print(f'{n}!={myFactorial(n)}')
