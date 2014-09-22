#!/usr/bin/python

import os
import argparse

parser = argparse.ArgumentParser(description='Create symlinks to dotfiles')
parser.add_argument('-f', '--force', action='store_true', help='override existing symlinks')
args = parser.parse_args()

home = os.path.expanduser('~')

for root, dirs, files in os.walk('.'):
    for filename in files:
        if filename.endswith('.symlink'):
            new_file = home + '/.' + filename[:-8]
            file_path = os.path.abspath(root) + '/' + filename
            if os.path.isfile(new_file):
                if args.force:
                    os.unlink(new_file)
                    os.symlink(file_path, new_file)
                    print "Overrode symlink @ {} with {}!".format(new_file, file_path)
                else:
                    print "Skipped existing symlink to {} @ {}!".format(file_path, new_file)
            else:
                os.symlink(file_path, new_file)
                print "Created symlink to {0} @ {1}!".format(file_path, new_file)
