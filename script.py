#!/usr/bin/env python

# a python script that does this, and that.

import errno
import os
import stat

main_dir = os.path.expanduser('~/.ga-tests')
sub_dir = os.path.join(main_dir, 'sub')

try:
	os.mkdir(main_dir)
except OSError as e:
	if e.errno != errno.EEXIST:
		print('fatal: 1')
		sys.exit(1)

try:
	os.mkdir(sub_dir, stat.S_IRWXU)
except OSError as e:
	if e.errno != errno.EEXIST:
		print('fatal: 2')
		sys.exit(1)

print('success')
