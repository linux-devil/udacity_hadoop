#!/usr/bin/env python
import sys
count = 0
for line in sys.stdin:
	data = line.strip().split()
	try:
		#ip,ident,username,time,gmt,req,status,obj = data
		print data
	except:
		pass