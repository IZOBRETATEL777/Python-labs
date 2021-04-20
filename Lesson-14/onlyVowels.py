print('Enter a string')
s = input()
vowels = 'аоуыиэеёюя'
for i in s:
    if i in vowels:
        print(i, end=' ')
print()
