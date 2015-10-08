#!/usr/bin/env python3
#

import _thread, time

def counter(myId, count):
	# print(count)
	for i in range(count):
		# time.sleep(1)
		mute.acquire()
		print('[%s] => %s' % (myId, i))
		mute.release()
	exitmutexes[myId].acquire()


mute = _thread.allocate_lock()
exitmutexes = [_thread.allocate_lock() for i in range(10)]
for i in range(10):
	_thread.start_new_thread(counter, (i, 100))

for mutex in exitmutexes:
	while not mutex.locked():
		# pass
		print('Main thread is waiting....')
print('Main thread exiting')