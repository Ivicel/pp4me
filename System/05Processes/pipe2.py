#!/usr/bin/env python3
#
#
import os, time
import pdb

def child(pipeout):
	zzz = 0
	while True:
		time.sleep(zzz)
		msg = ('Spam %03d\n' % zzz).encode()
		os.write(pipeout, msg)
		zzz = (zzz + 1) % 5

def parent():
	pipein, pipeout = os.pipe()
	if os.fork() == 0:
		os.close(pipein)
		child(pipeout)
	else:
		# pdb.set_trace()
		# os.close(pipeout)
		fd = os.fdopen(pipein)
		while True:
			# line = os.read(pipein, 32)
			line = fd.readline(32)
			print('Parent %d got [%s] at %s' % (os.getpid(), line[:-1], time.time()))

if __name__ == '__main__':
	parent()
