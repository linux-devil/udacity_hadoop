#!/usr/bin/env python
import sys
last_key = None
summ=0
for line in sys.stdin:
	key,value = line.strip().split("\t")
	value = float(value)
	if last_key and key!=last_key:
		print "%s\t%s" %(last_key,summ)
		summ= 0	
	last_key = key
	summ = max(value,summ)
print "%s\t%s" %(last_key,summ)