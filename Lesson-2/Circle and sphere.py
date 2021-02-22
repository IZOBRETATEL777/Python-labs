from math import pi
from random import randint

r = randint(1, 20)
print('Radius is', r)

# area of circle: pi*(r^2)
s = pi * r ** 2

# volume of sphere 3/4*pi*(r^3)
v = 4/3 * pi * r ** 3

print('Circle area is {:10.2f}'.format(s))
print('Sphere volume is {:10.2f}'.format(v))
