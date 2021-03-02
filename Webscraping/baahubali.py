from bs4 import BeautifulSoup
import requests
url = "https://en.wikipedia.org/wiki/Baahubali%3A_The_Beginning"

r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data,"html5lib")

#Get all links
for link in soup.find_all('a'):
    print(link.getText())


#Get all headings
for heading in soup.find_all('h1'):
    print(heading.text)
    
#Get all images
for image in soup.find_all('img'):
    print(image.get('src'))
