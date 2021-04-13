from random import randint


def bubble_sort(a):
    cnt = 0
    for i in range(0, len(a) - 1):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                cnt += 1
    return cnt


def selection_sort(a):
    cnt = 0
    for i in range(len(a) - 1):
        idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[idx]:
                idx = j
        if idx != i:
            a[i], a[idx] = a[idx], a[i]
            cnt += 1
    return cnt


n = 1000
run = 5
cntBub = 0
cntSel = 0
print('Wait...')
for i in range(run):
    a = [randint(1, 100) for _ in range(n)]
    b = a[:]
    cntBub += bubble_sort(a)
    cntSel += selection_sort(b)
print(f'Average for bubble sort is {cntBub // run}')
print(f'Average for selection sort is {cntSel // run}')



