n1, n2, n3, n4, n5 = map(int, input("Enter five integers in one line:\n").split())
ans = n1
if n2 > ans:
    ans = n2
if n3 > ans:
    ans = n3
if n4 > ans:
    ans = n4
if n5 > ans:
    ans = n5
print('Max of the given five numbers is', ans)
