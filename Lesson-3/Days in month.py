s = input('Enter name of month. First letter should be in upper case!\n')
if s == 'December' or s == 'January' \
        or s == 'March' or s == 'May'\
        or s == 'July' or s == 'August'\
        or s == 'October':
    ans = '31'
elif s == 'April' or s == 'June' or s == 'September' or s == 'November':
    ans = '30'
elif s == 'February':
    ans = '28 or 29'
else:
    ans = 'none'
if ans == 'none':
    print('You have written name incorrectly. Try again.')
else:
    print("There are " + ans + " days in given month.")
