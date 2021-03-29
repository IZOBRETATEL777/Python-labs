n = int(input())
a = [int(x) for x in input().split()]
neg = []
zero = 0
pos = []
for i in a:
    if i < 0:
        neg.append(i)
    if i == 0:
        zero += 1
    if i > 0:
        pos.append(i)
print(*pos, *([0] * zero), *neg, sep=' ')

