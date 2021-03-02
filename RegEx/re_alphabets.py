##returns the lines with only characters
import re
file    = "input.txt"
pattern = "^[a-zA-Z]+$"  
f=open(file,'r')

for lineno,line in enumerate(f):
     if re.search(pattern,line):
        print(lineno + 1,line.rstrip())

f.close()


