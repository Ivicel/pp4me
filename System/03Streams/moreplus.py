#!/usr/bin/env python3

import sys

def getreply():
	if sys.stdin.isatty():
		return sys.stdin.read(1)
	else:
		if sys.platform[:3] == 'win':
			import msvcrt
			msvcrt.putch(b'?')
			key = msvcrt.getche()
			return key
		else:
			return open('/dev/tty').readline()[:-1]

def more(text, numlines = 10):
	lines = text.splitlines()
	while lines:
		chunk = lines[:numlines]
		lines = lines[numlines:]
		for line in chunk:
			print(line)
		
		if lines and getreply() not in ['y', 'Y']:
			break

if __name__ == '__main__':
	if len(sys.argv) == 1:
		more(sys.stdin.read())
	else:
		more(open(sys.argv[1]).read())