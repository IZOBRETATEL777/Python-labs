while True:
    n = int(input('Enter N: '))
    if n <= 0:
        print('Enter natural number!')
    else:
        break
print('Number till N (N included) divisible by each of its digits')
for i in range(1, n + 1):
    m = i
    while m % 10 != 0 and i % (m % 10) == 0:
        m //= 10
    if m == 0:
        print(i, end=' ')
print()
