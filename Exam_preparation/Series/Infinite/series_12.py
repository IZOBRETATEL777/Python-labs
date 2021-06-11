ans = 0
i = 1
while True:
    term = 1 / ((2 * i - 1) * (2 * i + 1)) ** (1 / 2)
    if term <= 0.000001:
        break
    ans += term
    i += 1
print(f'{ans:.8f}')


