#!/usr/bin/env python
import sys
count =0
for line in sys.stdin:
	key,value = line.strip().split()
	count+=int(value)
print count