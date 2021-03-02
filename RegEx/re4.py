import re

mobile = re.compile(r'\b0?[7-9]\d{9}\b')
blankline = re.compile(r'^$')

#searching

text="My mobile number is 9866611005. My atm pin in 3456"
text1="My mobile numbers are 09090909090 8989898989 9866611005 09866611006 7866611005,986661100. My atm pin in 3456"

r=mobile.search(text)
print(r.group())
print(r.span())
print(re.findall(mobile,text1))



