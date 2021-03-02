import requests
from bs4 import BeautifulSoup
 
URL = "https://www.passiton.com/inspirational-quotes"
print("Getting data from the url")
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
quotes = soup.find('div', attrs = {'id':'all_quotes'})

out=open("inspirational-quotes.txt","w",encoding="utf-8")
 
for quotecount,row in enumerate(quotes.findAll('img')):
	quote=row.get("alt")
	print("Writing quote ", quotecount + 1)
	out.write(quote.split(".")[0] + "\n")
out.close()
		
		
		
#code based on https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
