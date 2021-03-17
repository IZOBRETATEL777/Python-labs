def divs(n, i = 2):
    if i > n:
        return
    while n % i == 0:
        print(i, end='')
        n //= i
        if n >= i:
            print('*', end='')
    divs(n, i + 1)


n = int(input())
divs(n)
print(f'={n}')
