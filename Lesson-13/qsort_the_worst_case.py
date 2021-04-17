def generator(n):
    a = [i for i in range(1, n + 1)]
    t = a[:]
    #print(*a)
    for i in range(0, n - 2):
        idxMid = a.index(t[i])
        #print(t[i], t[i + (n - i - 1) // 2])
        idxToSwp = a.index(t[i + (n - i - 1) // 2])
        a[idxMid], a[idxToSwp] = a[idxToSwp], a[idxMid]
        #print(*a)
    return a


cntQ = 0
cntBub = 0


def qSort(a, s, f):
    if s >= f:
        return
    global cntQ
    l = s
    r = f
    m = a[l + (r - l) // 2]
    while l <= r:
        while a[l] < m:
            l += 1
        while a[r] > m:
            r -= 1
        if l <= r:
            a[l], a[r] = a[r], a[l]
            l += 1
            r -= 1
            cntQ += 1
    qSort(a, s, r)
    qSort(a, l, f)


def bubbleSort(a):
    global cntBub
    for i in range(0, len(a) - 1):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                cntBub += 1


n = 10
# Max complexity:
#a = [1, 4, 6, 8, 10, 5, 3, 7, 2, 9]
#a = generator(n)

#Max number of swaps
a = [8, 7, 9, 10, 6, 1, 2, 3, 4, 5]

b = a[:]
print('Array:')
print(*a)
qSort(a, 0, n - 1)
print('The number of operations in Quick sort:', cntQ)
bubbleSort(b)
print('The number of operations in Bubble sort:', cntBub)
