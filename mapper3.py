#!/usr/bin/env python
import sys
count = 0
for line in sys.stdin:
	data = line.strip().split("\t")
	try:
		date,time,store,item,cost,payment = data
		print "{0}\t{1}".format(1,cost)
	except:
		pass