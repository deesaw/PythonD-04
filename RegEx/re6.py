#program to return the lines which has digits in it 
import re
file    = "input.txt"
pattern=r"\d+"      #returns the lines which has digits in the line
f=open(file,'r')
for lineno,line in enumerate(f):
     if re.search(pattern,line):
        print(lineno + 1,line.rstrip())

f.close()


