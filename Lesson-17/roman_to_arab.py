romanDigits = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
arabDigits = [1, 5, 10, 50, 100, 500, 1000]


def getValue(s):
    global romanDigits, arabDigits
    if s not in romanDigits:
        return -1;
    else:
        return arabDigits[romanDigits.index(s)]


def romanToArabic(s):
    res = 0
    i = 0
    while i < len(s) - 1:
        dig1 = getValue(s[i])
        dig2 = getValue(s[i + 1])
        if dig1 < dig2:
            res = res - dig1 + dig2
            i += 1
        else:
            res += dig1
        i += 1
    if i == len(s) - 1:
        res += getValue(s[i])
    return res
    

ss = input('Введите строку:\n')
s = ss.split()
for i in s:
    isRoman = 1
    for j in i:
        isRoman &= (getValue(j) != -1)
    if isRoman:
        ss = ss.replace(i, str(romanToArabic(i)), 1)
print('Результат:')
print(ss)

