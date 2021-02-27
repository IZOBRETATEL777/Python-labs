a, b, c = map(int, input().split())
if b + c > a and b + a > c and c + b > a:
    if a == b and b == c:
        print('equilateral')
    elif a != b and b != c and a != c:
        print('versatile')
    else:
        print('isosceles')
else:
    print('invalid')
