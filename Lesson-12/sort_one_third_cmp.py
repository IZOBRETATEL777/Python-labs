from random import randint


def asc_cmp(a, b):
    return a < b


def desc_cmp(a, b):
    return a > b

def selection_sort(a, cmp):
    for i in range(len(a)):
        idx = i
        for j in range(i + 1, len(a)):
            if cmp(a[j], a[idx]):
                idx = j
        if idx != i:
            a[i], a[idx] = a[idx], a[i]
    return a


n = 15
a = [randint(1, 100) for _ in range(n)]
print('Array:')
print(*a)
a = selection_sort(a[:n//3], asc_cmp) + selection_sort(a[n//3:n//3*2], desc_cmp) + selection_sort(a[n//3*2:], asc_cmp)
print('Sorted:')
print(*a)

