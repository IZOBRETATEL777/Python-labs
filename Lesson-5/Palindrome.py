n = abs(int(input('Enter integer: ')))
n1 = n
rev = 0
while n1 > 0:
    rev = rev * 10 + n1 % 10
    n1 //= 10
if n == rev:
    print('It is palindrome!')
else:
    print('It is not palindrome')
    
