#Program to get lines which has IFSC code
import re
file    = "input.txt"
pattern = "^[a-zA-Z]{4}\d{7}$"  #returns the lines with only characters

f=open(file,'r')

#ifsccode='HDFC0000003'
ifsc="[]"
for lineno,line in enumerate(f):
     if re.search(pattern,line):
        print(lineno + 1,line.rstrip())

f.close()


