#main program
n = int(input('Enter tagret boundary: '))
ans = 0
for i in range(1, n + 1):
    term = 1 / ((3 * i - 2) * (3 * i + 1))
    ans += term
print(f'{ans:.3f}')


