from random import randint


def getSecond(n):
	while n > 99:
		n //= 10
	return n % 10


def selection_sort(a):
    for i in range(len(a) - 1):
        idx = i
        for j in range(i + 1, len(a)):
            if getSecond(a[j]) > getSecond(a[idx]):
                idx = j
        if i != idx:
            a[i], a[idx] = a[idx], a[i]
    return a


n = 20
a = [randint(1000, 9000) for _ in range(n)]
print('Array:')
print(*a)
print('\nSorted by second digit:')
print(*selection_sort(a))

