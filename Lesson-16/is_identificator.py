s = input('Enter a word:\n')
res = (s[0].isalpha() or s[0] == '_')
for i in s:
    res &= (i.isalpha() or i.isdigit() or i == '_')
if res:
    print('It is an identificator')
else:
    print('It is not an identificator')

