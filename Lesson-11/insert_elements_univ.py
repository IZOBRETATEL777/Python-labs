from random import randint


def ins(idx, val, a):
    a.append(-1)
    for i in range(len(a) - 1, idx, -1):
        a[i] = a[i - 1]
    a[idx] = val
    return a


def getIdx(idx, idxTable):
    for i in range(len(idxTable)):
        if idxTable[i] == idx:
            return i
    return -1


n = 20
a = [randint(1, 100) for _ in range(n)]
idxTable = [i for i in range(n)]
print('Array:')
print(*a, sep=' ')
for _ in range(2):#range can be changed
    print('Enter an index and value to insert in one line:')
    idx, val = map(int, input().split())
    idx = getIdx(idx, idxTable)
    if idx == -1:
        print('Error')
        continue
    a = ins(idx, val, a)
    idxTable = ins(idx, -1, idxTable)
print('Inserted!')
print(*a, sep=' ')


