s = input('Enter a string:\n')
low = 0
upper = 0
for i in s:
    if ord('a') <= ord(i) <= ord('z'):
        low += 1
    elif ord('A') <= ord(i) <= ord('Z'):
        upper += 1
print('There are', upper, 'letters in upper case and', low, 'in lower case')
