def sort_three(a1, a2, a3):
    a1, a2 = min(a1, a2), max(a1, a2)
    a2, a3 = min(a2, a3), max(a2, a3)
    a1, a2 = min(a1, a2), max(a1, a2)
    return a1, a2, a3


a, b, c = map(int, input().split())
print(*sort_three(a, b, c), sep=' ')
