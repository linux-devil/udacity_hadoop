#!/usr/bin/env python
import sys

for line in sys.stdin:
	data = line.strip().split("\t")
	try:
		date,time,store,item,cost,payment = data
		print "{0}\t{1}".format(item,cost)
	except:
		pass