from bs4 import BeautifulSoup
import requests
url = "https://www.python.org/downloads/"

r  = requests.get(url)

soup = BeautifulSoup(r.text,"html5lib")


#Get all links
for link in soup.find_all('a'):
    print(link.get('href'))


