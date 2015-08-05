#!/usr/bin/env python3


#input: 9 + (3 - 1) * 3 + 10 / 2
#output: 9 3 1 - 3 * + 10 2 / +

import sys

def convert(express):
	exp = list(express.strip())
	result = []
	stack = []
	for n in exp:
		if n.isdigit():
			result.append(' ' + n + ' ')
		elif n == ' ':
			continue
		elif n in ['+', '-', ')']:
			if n == ')':
				t = ''.join(stack).rsplit('(', 1)
				stack = list(t[0])
				result.append(t[1][-1::-1])
			else:
				l = stack[-1::-1]
				#result += [stack.pop() for m in l[:l.index('(')]]
				for k in stack[-1::-1]:
					if k != '(':
						result.append(stack.pop())
					else:
						break
				stack.append(n)
		elif n in ['/', '*', '(']:
			if stack[-1:] in ['/', '*']:
				result.append(stack.pop())
			stack.append(n)
		else:
			raise ValueError('Only can input "+-*/()"')
	else:
		return ''.join(result + stack[-1::-1])

if __name__ == '__main__':
	result = convert(sys.argv[1])
	print('The "%s" convert to: "%s"' % (sys.argv[1], result))