print('Enter a string:')
s = input()
idx = 0
while s[idx] == ' ':
    idx += 1
if s[0] == ' ':
    s = s[idx:]
print('Fixed:')
print(s)

