from random import randint


n = int(input('Введите длину массива: '))
a = [randint(0, 5) for _ in range(n)]
print('Массив:')
print(*a, sep=' ')
ans = []
for i in range (0 , n - 1):
    if a[i + 1] == a[i] and a[i] not in ans:
        ans += [a[i]]
if len(ans) == 0:
    print('Нет')
else:
    print('Есть:', *ans, sep=' ')
