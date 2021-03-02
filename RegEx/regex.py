#regex examples
import re
#finding

#find any number anywhere in the string

print(re.findall("\d+","3 pens cost 20 rupees and 50 paise"))

#find any number at the begining of the string
print(re.findall("^\d+","3 pens cost 20 rupees and 50 paise"))

#find any number at the end of the string
print(re.findall("\d+$","3 pens cost 20 rupees and 50"))






#Split with multiple separaters
print(re.split("[,:-]","Ramesh,223-rsannareddy@gmail.com:male"))


























text="My mobile is 9885970033. My atm pin in 3487"



print( re.sub(r'\d','*',text))
print( re.sub(r'\d+','*',text))
print( re.sub(r'0?[7-9]\d{9}','*',text))





text="My mobile is 9885970033. My atm pin in 3487"
r=re.search('0?[7-9]\d{9}',text)
print(r.group())
print(r.span())





















#compiled regex
number = re.compile('\d+')
result=number.findall('He has 13 blue pens, 9 balls and 20 rupees')
print result









number = re.compile('\d+')
it=number.finditer('He has 13 blue pens, 9 balls, 6 books and 20 rupees')
for match in it:
	print match.span()


	
	
	
	
	
	
	
	
	

	
	
	
	
#compiled regex
mobile = re.compile('0?[7-9]\d{9}')
text="I stay at 502,HIG 292,KPHB. You can reach me on 9885970033"

x=mobile.findall(text)
print(x)



result=r.findall('He has 13 blue pens, 9 balls, 6 books and 20 rupees')
print result


print(re.sub(r'\sAND\s', ' & ', 'A and B And C', flags=re.IGNORECASE))
