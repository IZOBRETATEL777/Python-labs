print('Введите целые числа (каждое в новой строке). Для остановки введите 0.')
inp = int(input())
last  = inp
isSorted = True
while True:
    inp = int(input())
    if inp == 0:
        break
    isSorted &= (inp >= last)
    last = inp
if isSorted:
    print('Отсортировано')
else:
    print('Неотсортировано')

