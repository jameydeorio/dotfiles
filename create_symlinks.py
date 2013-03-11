#!/usr/bin/python

import os

files_to_symlink = []
curdir = os.path.abspath('.')
home = os.path.expanduser('~')

for root, dirs, files in os.walk(curdir):
	for filename in files:
		if filename.endswith('.symlink'):
			new_filename = filename[:-8]
			file_path = root + '/' + filename
			os.symlink(file_path, home + '/.' + new_filename)
			print "Created symlink to {0} @ {1}!".format(file_path, home + '/.' + new_filename)
