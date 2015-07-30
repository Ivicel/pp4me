#!/usr/bin/env python3

import pickle
from db import db

filename = 'pickle_dbfilename'

def dump_db_file(db, filename):
	f = open(filename, 'wb')
	pickle.dump(db, f)
	f.close()

def load_db_file(filename):
	f = open(filename, 'rb')
	db = pickle.load(f)
	f.close()
	return db

def update_db_file(filename):
	database = load_db_file(filename)
	print('Before: %d' % database['sue']['pay'])
	database['sue']['pay'] *= 1.5
	print('After: %d' % database['sue']['pay'])
	dump_db_file(database, filename)


if __name__ == '__main__':
	dump_db_file(db, filename)
	update_db_file(filename)

