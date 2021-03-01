s1, s2, s3 = 'Антон', 'Борис', 'Виктор'

# input (names in the Possessive case)
a1 = int(input(f'Возраст {s1}a: '))
a2 = int(input(f'Возраст {s2}a: '))
a3 = int(input(f'Возраст {s3}a: '))

# bobble sort manual implementation
if a1 > a2:
    a1, a2 = a2, a1
    s1, s2 = s2, s1
if a2 > a3:
    a2, a3 = a3, a2
    s2, s3 = s3, s2
if a1 > a2:
    a1, a2 = a2, a1
    s1, s2 = s2, s1

print('Отввт:', end=' ')
if a1 == a3:
    print('У всех одинаковый возрат')
elif a2 == a3:
    print(f'{s2} и {s3} старше {s1}a')
else:
    print(f'{s3} старше всех')
