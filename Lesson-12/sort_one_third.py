from random import randint


def asc_sort(a):
    for i in range(len(a)):
        idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[idx]:
                idx = j
        if idx != i:
            a[i], a[idx] = a[idx], a[i]
    return a


def desc_sort(a):
    for i in range(len(a)):
        idx = i
        for j in range(i + 1, len(a)):
            if a[j] > a[idx]:
                idx = j
        if idx != i:
            a[i], a[idx] = a[idx], a[i]
    return a


n = 15
a = [randint(1, 100) for _ in range(n)]
print('Array:')
print(*a)
a = asc_sort(a[:n//3]) + desc_sort(a[n//3:n//3*2]) + asc_sort(a[n//3*2:])
print('Sorted:')
print(*a)

