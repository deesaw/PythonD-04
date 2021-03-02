from bs4 import BeautifulSoup
import requests
import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet("cars")
url='https://www.cardekho.com/used-cars+in+hyderabad'
r = requests.get(url)
data=r.text
soup = BeautifulSoup(data,'html.parser')
li='gsc_col-sm-12 gsc_col-md-12  holder'
taglist=["title","price","dotlist"]
count=0
row=0
col=0
for row,link in enumerate(soup.find_all(class_=taglist)):

	print(link)
	if "title" in link:
			print(count)
			
			ws.write(row,0,link.text)
			count+=1
	
	
		
wb.save("cities2.xls")   
  
