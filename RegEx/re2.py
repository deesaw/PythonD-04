import re
#Search:searches only at the first instance of a string
#match: matches at the begining of the string


text="My mobile is 9866611005. My atm pin in 3456 09866611015 "

r=re.search('(\+91)?0?[7-9]\d{9}',text)
print("r.group()...",r.group())
print("r.span()...",r.span())


text2="is my mobile number"
r2=re.match('0?[7-9]\d{9}',text2)
print(r2)
print(r2.group())



