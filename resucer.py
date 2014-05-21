#!/usr/bin/env python
import sys
last_key = None
summ=0
summk = 0
for line in sys.stdin:
	key,value = line.strip().split("\t")
	summ+=float(value)	
	summk+=float(key)
print "%s\t%s" %(summk,summ)