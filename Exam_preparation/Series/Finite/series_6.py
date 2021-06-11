#main program
n = int(input('Enter tagret boundary: '))
ans = 0
for i in range(1, n + 1):
    term = 0.001 ** (1 / i)
    ans += term
print(f'{ans:.3f}')


