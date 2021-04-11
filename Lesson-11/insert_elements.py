from random import randint


def ins(idx, val, a):
    return a[:idx] + [val] + a[idx:]


n = 20
a = [randint(1, 100) for _ in range(n)]
idxTable = [i for i in range(n)]
print('Array:')
print(*a, sep=' ')
print('Enter an index and value to insert in one line:')
idx1, val1 = map(int, input().split())
a = ins(idx1, val1, a)
print('Enter an index and value to insert:')
idx2, val2 = map(int, input().split())
if idx1 <= idx2:
    idx2 += 1
a = ins(idx2, val2, a)
print('Inserted!')
print(*a, sep=' ')



