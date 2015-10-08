#!/usr/bin/env python3
#

import _thread, time

def counter(myId, count):
	# print(count)
	for i in range(count):
		time.sleep(1)
		mute.acquire()
		print('[%s] => %s' % (myId, i))
		mute.release()


mute = _thread.allocate_lock()
for i in range(5):
	_thread.start_new_thread(counter, (i, 5))

time.sleep(5)