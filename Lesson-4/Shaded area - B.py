x, y = map(float, input('Enter coordinates of point (x, y) in one line\n').split())
if (x ** 2 + y ** 2 <= 1 and y >= x and y >= -x) or (x ** 2 + y ** 2 <= 1 and y <= 0 and (y >= x or y >= -x)) or (x ** 2 + y ** 2 >= 1 and y <= x and y <= -x):
    print('The given point inside shaded area')
else:
    print('The given point is not inside shaded area')
