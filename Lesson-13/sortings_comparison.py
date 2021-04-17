from random import randint


cntBub = 0
cntSel = 0
cntQ = 0


def bubble_sort(a):
    global cntBub
    for i in range(0, len(a) - 1):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                cntBub += 1


def selection_sort(a):
    global cntSel
    for i in range(len(a) - 1):
        idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[idx]:
                idx = j
        if idx != i:
            a[i], a[idx] = a[idx], a[i]
            cntSel += 1


def quick_sort(a, s, f):
    global cntQ
    if s >= f:
        return
    m = a[s + (f - s) // 2]
    l = s
    r = f
    while l <= r:
        while a[l] < m: l += 1
        while a[r] > m: r -= 1
        if l <= r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
            cntQ += 1
    quick_sort(a, s, r)
    quick_sort(a, l, f)


n = 1000
run = 5
print('Wait...')
for i in range(run):
    a = [randint(1, 100) for _ in range(n)]
    bubble_sort(a[:])
    selection_sort(a[:])
    quick_sort(a, 0, n - 1)
print(f'Average for bubble sort is {cntBub / run}')
print(f'Average for selection sort is {cntSel / run}')
print(f'Average for quick sort is {cntQ / run}')
