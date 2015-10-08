#!/usr/bin/env python3
#
#
#
import os, sys
from pprint import pprint

trace = False
dirlist = sys.path
allsizes = []

for dirname in dirlist:
	if not os.path.isdir(dirname):
		continue
	for thisDir, subHere, filesHere in os.walk(dirname):
		if trace: 
			print(thisDir)
		for filename in filesHere:
			if trace:
				print('...', filename)
			if filename.endswith('.py'):
				fullname = os.path.join(thisDir, filename)
				fullsize = os.path.getsize(fullname)
				allsizes.append((fullsize, fullname))

allsizes.sort()
pprint(allsizes[:2])
pprint(allsizes[-2:])