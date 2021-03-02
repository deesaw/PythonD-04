from bs4 import BeautifulSoup
import requests
import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet("cars")
url='https://www.cardekho.com/used-cars+in+hyderabad'
r = requests.get(url)
data=r.text
soup = BeautifulSoup(data,'html.parser')


#print(soup.find_all("a"))
#<img class="hover imageTransition" title="2016 Tata Indica V2 eLS" 
'''for link in soup.find(class_='title'):
   car_d=link.text
   print(car_d)'''
count=0
'''
for link in soup.find_all(class_='dotlist'):
   print(count)
   car_d=link.text
   print(".#.#.#",car_d)
   count=count+1
li='gsc_col-sm-12 gsc_col-md-12  holder'
taglist=["title","price","dotlist"]
details=[]

# for link in soup.find_all(class_=taglist):
	# print("....",link)
	
	# car_d=link.text
	# print("####",car_d)
# for link in (taglist):
	# if link =='title':
		# for link1 in soup.find_all(class_=link):
			# print("....",link1)
			# car_title=link1.text
			# print("####",car_d)

'''
#ws.write(0,0,"Hyderabad")
#for row,line in enumerate(f):#read line by line
#ws.write(row,0,line.strip()) 
taglist=["title","price","dotlist"]
count=0
for link in (taglist):
	print(count)
	if link=="title":
		for link1 in soup.find_all(class_="title"):
			car_title=link1.text
			print("CAR TITLE:",link1.text)
			#ws.write()
		
	elif link=="dotlist":
		for link1 in soup.find_all(class_='dotlist'):
			print("@@@@@",link1.text)
				
	elif link=="price":
		for link1 in soup.find_all(class_="price"):
			car_price=link1.text
			print("CAR PRICE:",link1.text)
	count=count+1
			
		
	
	
	
	
	
   
   
