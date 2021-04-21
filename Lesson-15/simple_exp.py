s = input()
op1 = s.find('-')
if op1 < 0:
    op1 = s.rfind('+')
op2 = s.find('+')
if op2 < 0:
    op2 = s.rfind('-')
op1, op2 = min(op1, op2), max(op1, op2)
numbers = [int(s[:op1]), int(s[op1 + 1 : op2]), int(s[op2 + 1:])]
if s[op1] == '-':
    numbers[1] *= -1
if s[op2] == '-':
    numbers[2] *= -1
print(sum(numbers))

