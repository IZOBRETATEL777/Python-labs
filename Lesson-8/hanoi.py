def hanoi(n, k, m):
    if n == 0: return
    p = 6 - k - m
    hanoi(n - 1, k, p)
    print(k, "->", m)
    hanoi(n - 1, p, m)


hanoi(4, 1, 2)
