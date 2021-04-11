def bubble(a, n, cur=0):
    if n - 1 == cur:
        return a
    for i in range(n - 2, cur - 1, -1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    return bubble(a, n, cur + 1)


n = int(input("Enter size: "))
print('Enter array in one line:')
a = [int(i) for i in input().split()]
print('Sorted array:')
a = bubble(a, n)
print(*a, sep=' ')

