#calculation factorial
def myFactorial(n : int) -> int:
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


#main program
n = int(input('Enter tagret boundary: '))
ans = 0
for i in range(1, n + 1):
    term = (-1) ** i * i ** 2 / myFactorial(2 * i + 1)
    ans += term
print(f'{ans:.3f}')


