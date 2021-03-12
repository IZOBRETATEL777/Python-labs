def my_factorial(n):
    res = 1
    for i in range (2, n + 1):
        res *= i
    return res


n = int(input())
print(my_factorial(n))
