s = input('Enter a sentence:\n')
ans = ''
caps = True
for i in s:
    if caps:
        ans += i.upper()
    else:
        ans += i.lower()
    if i.isalpha():
        caps = not caps
print(ans)

    
