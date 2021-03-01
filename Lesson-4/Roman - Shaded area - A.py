x, y = map(float, input('Enter coordinates of point (x, y) in one line\n').split())
if (y <= x**2 and y >= 2 - x) or (y >= x**2 and x <= 0 and y <= 2 -x and y >= 4 - x ** 2) or \
        (y >= 0 and y >= x ** 2 and x >= 0 and y <= 2 - x) or (x >= 0 and y >= 4 - x ** 2 and y <= x ** 2):
    print('The given point inside shaded area')
else:
    print('The given point is not inside shaded area')
