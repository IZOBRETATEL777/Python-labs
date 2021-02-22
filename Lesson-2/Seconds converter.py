s = int(input('Enter time in seconds: '))
h = s // (60 * 60)
m = (s // 60) % 60
s = s % 60
print('It is {:d} hours, {:d} minutes, and {:d} seconds'.format(h, m, s))
