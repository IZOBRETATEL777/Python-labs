# calculating factorial
def myFactorial(n : int) -> int:
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res


#main program
n = int(input('Enter a right bound of the range: '))
ans = 0
for i in range(1, n + 1):
    term = ((-1) ** i * (myFactorial(i)) ** 2) / myFactorial(2 * i)
    ans += term
print(f'Result {ans:.3f}')


