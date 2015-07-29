#!/usr/bin/env python3

import sys

db = {
	'bob': {
		'job': 'dev',
		'pay': 300000,
		'age': 42,
		'name': 'Bob Smith'
	},
	'sue': {
		'job': 'hdw',
		'pay': 30000,
		'age': 45,
		'name': 'Sue Jones'
	},
	'tom': {
		'job': None,
		'pay': 0,
		'age': 50,
		'name': 'Tome'
	}
}

ENDREC = 'endrec.'
ENDDB = 'enddb.'
RECSEP = '=>'
dbfilename = 'dbfilename'

def storeDbase(db, dbfilename = dbfilename):
	file = open(dbfilename, 'a')
	for key in db:
		print(key, file = file)
		for (field, value) in db[key].items():
			print(field, repr(value), sep = RECSEP, file = file)
		print(ENDREC, file = file)
	print(ENDDB, file = file)
	file.close()

def loadDbase(dbfilename = dbfilename):
	dbfile = open(dbfilename)
	db = {}
	sys.stdin = dbfile

	while True:
		rec = {}
		key = input()
		if key == ENDDB:
			break
		rec = {}
		while True:
			field = input()
			if field == ENDREC:
				break
			name, value = field.split(RECSEP)
			rec[name] = value
		db[key] = rec
	return db



if __name__ == '__main__':
	pass