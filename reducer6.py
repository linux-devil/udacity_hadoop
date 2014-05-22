#!/usr/bin/env python
import sys
count =0
last_key = None
for line in sys.stdin:
	key,value = line.strip().split()
	value = int(value)
	if last_key and key != last_key:
		print "{0}\t{1}",%(last_key,count)
		count = 0
	last_key = key
	count+=value
print "{0}\t{1}"%(last_key,count)