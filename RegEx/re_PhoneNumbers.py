#returns the mobile numbers
import re
file    = "input.txt"
f=open(file,'r')
pattern=r"\b(0|(\+)|(91))?[6-9]\d{9}\b"

for lineno,line in enumerate(f):
     if re.search(pattern,line):
        print(lineno + 1,line.rstrip())

f.close()


