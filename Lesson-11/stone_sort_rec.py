def bubble(a, n):
    if n == 1:
        return a
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            a[i], a[i + 1] = a[i + 1], a[i]
    return bubble(a, n - 1)


n = int(input("Enter size: "))
print('Enter array in one line:')
a = [int(i) for i in input().split()]
print('Sorted array:')
a = bubble(a, n)
print(*a, sep=' ')

