def isPrime(n, i=2):
    if n == 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return isPrime(n, i + 1)


n = int(input())
print('YES' if isPrime(n) else 'NO')

