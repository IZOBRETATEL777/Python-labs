def toDigit(n):
    return chr(ord('A') + n - 10) if n > 9 else str(n)


def toDecDigit(n):
    return int(n) if n.isdigit() else ord(n) - ord('A') + 10


def toDec(s, base):
    power = 0
    n = 0
    for i in s[::-1]:
        n += toDecDigit(i) * (base ** power)
        power += 1
    return n


def createAlphabet(base):
    return [toDigit(i) for i in range(base)]


s = input('Enter a string:\n')
base = 2
alphabet = createAlphabet(base)
isNumber = True
for i in s:
    if i not in alphabet:
        isNumber = False
        break
if not isNumber:
    print('It is not a binary number')
else:
    print('It is a binary representation of', toDec(s, base))

