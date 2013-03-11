#!/usr/bin/python

import os


home = os.path.expanduser('~')

for root, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith('.symlink'):
            new_file = home + '/.' + filename[:-8]
            file_path = root + '/' + filename
            if os.path.isfile(new_file):
                print "Skipped existing symlink to {0} @ {1}!".format(file_path, new_file)
            else:
                os.symlink(file_path, new_file)
                print "Created symlink to {0} @ {1}!".format(file_path, new_file)

