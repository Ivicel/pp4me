#!/usr/bin/env python3
#
#
import os, sys, glob, time
from subprocess import Popen, PIPE

# configuration args
testdir = sys.argv[1] if len(sys.argv) > 1 else os.curdir
forcegen = len(sys.argv) > 2
print('Start tester:', time.asctime())
print('in', os.path.abspath(testdir))

def verbose(*args):
	print('-' * 80)
	for arg in args:
		print(arg)

def quiet(*args):
	pass

trace = quiet

# glob scripts to be tested
testpatt = os.path.join(testdir, 'Script', '*.py')
testfiles = glob.glob(testpatt)
testfiles.sort()
trace(os.getcwd(), *testfiles)

numfail = 0
for testpath in testfiles:
	testname = os.path.basename(testpath)

	# get input and args
	infile = testname.replace('.py', '.in')
	inpath = os.path.join(testdir, 'Inputs', infile)
	indata = open(inpath, 'rb').read() if os.path.exists(inpath) else b''

	argfile = testname.replace('.py', '.args')
	argpath = os.path.join(testdir, 'Args', argfile)
	argdata = open(inpath).read() if os.path.exists(argpath) else ''

	# locate output and error, scrub prior results
	outfile = testname.replace('.py', '.out')
	outpath = os.path.join(testdir, 'Outputs', outfile)
	outpathbad = outpath + '.bad'
	if os.path.exists(outpathbad): os.remove(outpathbad)

	errfile = testname.replace('.py', '.err')
	errpath = os.path.join(testdir, 'Errors', errfile)
	if os.path.exists(errpath): os.remove(errpath)

	# run test with redirected streams
	pypath = sys.executable
	command = '%s %s %s' % (pypath, testpath, argdata)
	trace(command, indata)

	process = Popen(command, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
	process.stdin.write(indata)
	process.stdin.close()
	outdata = process.stdout.read()
	errdata = process.stderr.read()
	trace(outdata, errdata, existstatus)

	# analyze results
	if existstatus != 0:
		print('ERROR status:', testname, errpath)
	if errdata:
		print('ERROR stream:', testname, errpath)
		open(errpath, 'wb').write(errdata)
	if existstatus or errdata:
		numfail += 1
		open(outpathbad, 'wb').write(outdata)
	elif not os.path.exists(outpath) or forcegen:
		print('generating:', outpath)
		open(outpath, 'wb').write(outdata)
	else:
		priorout = open(outpath, 'rb').read()
		if priorout == outdata:
			print('passed:', testname)
		else:
			numfail += 1
			print('FAILED output:', testname, outpathbad)
			open(outpathbad, 'wb').write(outdata)

	print('Finished:', time.asctime())
	print('%s tests were run, %s tests failed.' % (len(testfiles), numfail))