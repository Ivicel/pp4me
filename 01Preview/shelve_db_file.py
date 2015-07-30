#!/usr/bin/env python3

import shelve
from db import db

filename = 'shelve_db_file'

def dump_shelve_file(db, filename):
	data = shelve.open(filename)
	for key in db:
		data[key] = db[key]
	data.close()
	
def load_shelve_file(filename):
	data = shelve.open(filename)
	for key in data:
		print(key, data[key], sep = ' => ')




if __name__ == '__main__':
	dump_shelve_file(db, filename)
	load_shelve_file(filename)