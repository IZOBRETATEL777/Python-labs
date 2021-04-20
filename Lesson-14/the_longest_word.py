print('Введите строку:')
s = input()
haveSpace = True
ans = ''
cur = ''
for i in s:
    if i == ' ':
        if len(cur):
            haveSpace = False
            if len(cur) > len(ans):
                ans = cur;
            cur = ''
        else:
            haveSpace = True
    else:
        cur += i
if len(cur) > len(ans):
    ans = cur
print(f'Самое длинное слово: {ans}, длина {len(ans)}')




