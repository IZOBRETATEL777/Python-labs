from math import pi, cos

#convert degrees to radians
def toRadians(alpha : float) -> float:
    return alpha / 180 * pi


#main program
n = int(input('Enter tagret boundary: '))
x = toRadians(float(input('Enter X: '))) # input and covert to radians
ans = 0
for i in range(1, n + 1):
    term = cos(x ** i) / (i ** 2)
    ans += term
print(f'{ans:.3f}')


