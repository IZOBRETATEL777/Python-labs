s = input('Enter a word:\n')
res = (ord('A') <= ord(s[0]) <= ord('Z') or ord('a') <= ord(s[0]) <= ord('z') or s[0] == '_')
for i in s:
    res &= (ord('A') <= ord(s[0]) <= ord('Z') or ord('a') <= ord(s[0]) <= ord('z') or i.isdigit() or i == '_')
if res:
    print('It is an identificator')
else:
    print('It is not an identificator')

