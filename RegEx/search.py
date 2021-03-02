#This file takes two arguments pattern and filename
#It will search the file the print the lines matching
#the pattern along with the line numbers


import sys
import re
if len(sys.argv) == 3:
	pattern   = sys.argv[1]
	filename  = sys.argv[2]
elif len(sys.argv) == 1:
	pattern   = raw_input("Enter pattern ")
	filename  = raw_input("Enter filename ")
else:
	print("Usage : {} <pattern> <file>".format(sys.argv[0]))
	sys.exit(1)

f=open(filename,'r')

for lineno,line in enumerate(f):
	if re.search(pattern,line):
		print(lineno + 1,line.rstrip())
#close the file
f.close()
