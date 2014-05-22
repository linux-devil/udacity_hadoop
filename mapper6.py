#!/usr/bin/env python
import re
import sys
from collections import defaultdict, namedtuple
format_pt = re.compile(
			r"(?P<host>[\d\.]+) (?P<identity>\S*) (?P<user>\S*) \[(?P<time>.*?)\] " r'"(?P<request>.*?)"\s'
			 r"(?P<status>\d+) (?P<bytes>\S*)")
Access = namedtuple('Access',['host','identity','user','time','request',
					'status','bytes','referer','user_agent'])
count = 0
for line in sys.stdin:
	x = format_pt.match(line.rstrip())
	try:
		if x.group('request'):
			k = x.group('request').split(' ')
			print "{0}\t{1}".format(k[1],1)
		else:
			pass
	except:
		pass