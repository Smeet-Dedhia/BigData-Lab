#!/usr/bin/python
"""mapper.py"""

import sys
#input comes from STDIN
for line in sys.stdin:
#remove leading and trailing whitespace
     line=line.strip()
#split the line into words
     words=line.split()
#increase counters
     for word in words:
#write the results to STDOUT
#tab-delimited; the trivial word count is 1
         print('%s\t%s'%(word,1))
         
