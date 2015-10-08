#!/usr/bin/env python3
#
#
import os, time
import sys

def child():
	zzz = 0
	pipeout = os.open(filename, os.O_WRONLY)
	while True:
		time.sleep(zzz)
		msg = ('Spam %03d\n' % zzz).encode()
		os.write(pipeout, msg)
		zzz = (zzz + 1) % 5

def parent():
	pipein = os.open(filename, os.O_RDONLY)
	fd = os.fdopen(pipein)
	while True:
		# line = os.read(pipein, 32)
		line = fd.readline()
		print('Parent %d got [%s] at %s' % (os.getpid(), line[:-1], time.time()))

if __name__ == '__main__':
	filename = 'fifo.tmp'
	if not os.path.exists(filename):
		os.mkfifo(filename)
	if len(sys.argv) == 1:
		parent()
	else:
		child()
