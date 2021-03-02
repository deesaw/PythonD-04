#regex examples
import re
#finding

#find any number anywhere in the string

print(re.findall("\d","3 pens cost 20 rupees and 50 paise"))

print(re.findall("\d+","3 pens cost 20 rupees and 50 paise"))

#find any number at the begining of the string
print(re.findall("^\d+","3 pens cost 20 rupees and 50 paise"))

#find any number at the end of the string
print(re.findall("\d+$","3 pens cost 20 rupees and 50 paise "))

#Split with multiple separaters
print(re.split("[,:-]","Lakshmi,276-plakshmipriya@gmail.com:female"))

