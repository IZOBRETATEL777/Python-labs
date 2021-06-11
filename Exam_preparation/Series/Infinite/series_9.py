i = 1
ans = 0
while True:
    term = 1 / ((3 * i - 2) * (3 * i + 1))
    if term <= 0.000001:
        break
    ans += term
    i += 1
print(f'{ans:.8f}')


