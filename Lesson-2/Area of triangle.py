from math import sqrt

print('Enter sides of triangle')

# input
a = float(int(input('Enter a: ')))
b = float(int(input('Enter b: ')))
c = float(int(input('Enter c: ')))

# using Heron's formula formula
p = (a + b + c) / 2
area = sqrt(p * (p - a) * (p - b) * (p - c))

print('Area of the given triangle is {:.2f}'.format(area))
