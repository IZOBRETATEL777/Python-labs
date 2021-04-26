def parse(exp):
	parsedEx = []
	i = 0
	while i < len(exp):
		t = exp[i]
		if (not t.isdigit()):
			parsedEx.append(t)
			i += 1
		else:
			t = ''
			while i < len(exp) and (exp[i].isdigit() or exp[i] == '.'):
				t += exp[i]
				i += 1
			parsedEx.append(int(t))
	return parsedEx


def toRPN(parsedEx):
	st = []
	output = []
	prior = [-1, -2, 2, 1, '_', 1, '_', 2]
	#		[40, 41, 42, 43, 44, 45, 46, 47]
	"""
	{
		')':-2, #41
		'(':-1, #40
		'+':1,  #43
		'-':1,  #45
		'*':2,	#42
		'/':2	#47
	}
	"""
	for i in parsedEx:
		if (type(i) != str ):
			output.append(i)
		elif len(st) == 0 or i == '(':
			st.append(i)
		elif i == ')':
			while len(st) > 0 and st[-1] != '(':
				output.append(st[-1])
				st.pop()
			if len(st) > 0:
				st.pop()
		else:
			while len(st) > 0 and prior[ord(i) - 40] <= prior[ord(st[-1]) - 40]:
				output.append(st[-1])
				st.pop()
			st.append(i)
	while len(st) > 0:
		output.append(st[-1])
		st.pop()
	return output


def solveRPN(expr):
	st = []
	for i in expr:
		if type(i) != str:
			st.append(i)
		else:
			x = st[-1]
			st.pop()
			y = st[-1]
			st.pop()
			if i == '+':
				st.append(x + y)
			if i == '-':
				st.append(x - y)
			if i == '*':
				st.append(x * y)
			if i == '/':
				st.append(x // y)
	return st[-1]


def solve(exp):
	return solveRPN(toRPN(parse(exp)))


s = (input('Введите выражение: \n'))
print('Ответ:', solve(s))
