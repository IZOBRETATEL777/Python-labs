x, y = map(float, input('Enter coordinates of point (x, y) in one line\n').split())
if (y >= x and x <= 0 and x ** 2 + y ** 2 <= 1) or (y >= -x and x <= 0 and x ** 2 + y ** 2 <= 1) \
        or (x ** 2 + y ** 2 <= 1 and y >= 0 and (y >= -x and x <= 0 or y >= x and x >= 0)) \
        or (x ** 2 + y ** 2 >= 1 and y <= 0 and (y >= x and x <= 0 or x >= 0 and y <= x)):
    print('The given point inside shaded area')
else:
    print('The given point is not inside shaded area')
