# 'Да.' if contains two equal digits otherwise 'Нет.'

n = int(input('Введите натуральное число:\n'))

# manual dictionary structure interpretation
haveZero = 0
haveOne = 0
haveTwo = 0
haveThree = 0
haveFour = 0
haveFive = 0
haveSix = 0
haveSeven = 0
haveEight = 0
haveNine = 0

while n > 0:
    d = n % 10
    if d == 0:
        haveZero += 1
    elif d == 1:
        haveOne += 1
    elif d == 2:
        haveTwo += 1
    elif d == 3:
        haveThree += 1
    elif d == 4:
        haveFour += 1
    elif d == 5:
        haveFive += 1
    elif d == 6:
        haveSix += 1
    elif d == 7:
        haveSeven += 1
    elif d == 8:
        haveEight += 1
    elif d == 9:
        haveNine += 1
    n //= 10
if haveZero > 1 or haveOne > 1 or haveTwo > 1 or haveThree > 1 or haveFour > 1 or haveFive > 1 or haveSix > 1 or haveSeven > 1 or haveEight > 1 or haveNine > 1:
    print('Да. \nПовторяются:', end=' ')
    if haveZero > 1:
        print('0', end=' ')
    if haveOne > 1:
        print('1', end=' ')
    if haveTwo > 1:
        print('2', end=' ')
    if haveThree > 1:
        print('3', end=' ')
    if haveFour > 1:
        print('4', end=' ')
    if haveFive > 1:
        print('5', end=' ')
    if haveSix > 1:
        print('6', end=' ')
    if haveSeven > 1:
        print('7', end=' ')
    if haveEight > 1:
        print('8', end=' ')  
    if haveNine > 1:
        print('9', end=' ')
    print()
else:
    print('Нет.')
