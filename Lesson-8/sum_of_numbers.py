def sumOfNumbers(n):
    if n == 1:
        return n
    return sumOfNumbers(n - 1) + n

while True:
    n = int(input('Enter a natural number: '))
    if n <= 0:
        print('Try again')
    else:
        break
print('Sum of numbers between 1 and N is', sumOfNumbers(n))
