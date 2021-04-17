from random import randint


def selectionSort(a, start=0):
    if start == len(a) - 2:
        return
    idx = start
    for i in range(start + 1, len(a)):
        if a[idx] > a[i]:
            idx = i
    if start != idx:
        a[start], a[idx] = a[idx], a[start]
    selectionSort(a, start + 1)


n = 20
a = [randint(1, 100) for _ in range(n)]
print('Array:')
print(*a)
selectionSort(a)
print('Sorted:')
print(*a)
