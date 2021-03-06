a, b, c, n = 15, 17, 21, 185

# ax + by + cz = d
cnt = 0
for i in range(0, n // a + 1):
    for j in range(0, (n - i * a) // b + 1):
        if (n - a * i - b * j) % c == 0:
                cnt += 1
                print('{:d} pcs of type one\n{:d} pcs of type two\n{:d} pcs of type three\n'.format(
                    i, j, (n - a * i - b * j) // c))

print(f'The number of possible combinations is {cnt}:\n')

