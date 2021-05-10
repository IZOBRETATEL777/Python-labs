from random import randint

n = 5
m = 5
a = [list(randint(10, 90) for _ in range(m)) for _ in range(n)]
print('Matrix:')
for i in a:
    for j in i:
        print(j, end=' ')
    print()
print()
s = 0
for i in range(n):
    s += sum(a[i][:i + 1])
print('Sum of the elemts located under the main diagonal (including):', s)


