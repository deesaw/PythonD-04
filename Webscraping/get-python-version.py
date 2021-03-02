import requests
from bs4 import BeautifulSoup

 
URL = "https://www.python.org/downloads/"
print("Getting data from the url")
r = requests.get(URL)
 
soup = BeautifulSoup(r.content, 'html5lib')
 
buttons = soup.find('p', attrs = {'class':'download-buttons'})

#j = soup.select(".download-for-current-os > div:nth-child(3) > p:nth-child(2) > a:nth-child(1)")
#print (j)


versions = buttons.findAll('a')
text =versions[0].text
print(text.split()[-1])

