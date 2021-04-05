a = []
s = 0
inp = 1
print('Введите целые числа (каждое в новой строке). Для остановки введите 0.')
while True:
    inp = int(input())
    if inp == 0:
        break
    s += inp
    a.append(inp)
print()
avg = s / len(a)
print(f'Среднее арифметическое: {avg:g}')
print('Больше среднего:')
for i in a:
    if i > avg:
        print(i, end=' ')
print('\n')
print('Меньше среднего:')
for i in a:
    if i < avg:
        print(i, end=' ')
print()

