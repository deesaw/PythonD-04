#Program to get lines which has mail ids
import re
file    = "input.txt"
pattern = r"^[\w.]+\@[\w.]+\.[a-zA-Z]{2,3}$"  

f=open(file,'r')

for lineno,line in enumerate(f):
     if re.search(pattern,line):
        print(lineno + 1,line.rstrip())

f.close()


