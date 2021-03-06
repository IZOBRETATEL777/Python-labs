while True:
    a, b = map(int, input('Enter boundaries (natural numbers) of the range in one line:\n').split())
    if a > b or a <= 0 or b <= 0:
        print('Error! Try again')
    else:
        break
atLeastOnce = False
for i in range(a, b + 1):
    k = 2
    while k * k <= i:
        if i % k == 0:
            break
        k += 1
    if k * k > i:
        atLeastOnce = True
        print(i, end=' ')
if not atLeastOnce:
    print('No prime numbers in the given range')
else:
    print()
