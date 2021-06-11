from math import pi, cos

#convert degrees to radians
def toRadians(alpha : float) -> float:
    return alpha / 180 * pi


#main program
x = toRadians(float(input('Enter X: '))) # input and covert to radians
ans = 0
i = 1
while True:
    term = cos(x ** i) / (i ** 2)
    if term <= 0.000001:
        break
    ans += term
    i += 1
print(f'{ans:.3f}')


