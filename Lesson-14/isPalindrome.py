def isPalindrome(s):
    n = len(s)
    for i in range(0, n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True


s = input('Enter a word: ')
if isPalindrome(s):
    print('It is a palindrome')
else:
    print('It is not a palindrome')

