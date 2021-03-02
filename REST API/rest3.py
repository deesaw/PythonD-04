import requests
url = "http://garuda.pythonanywhere.com/words"
print(requests.get(url).text)
print(requests.get(url+ "/water").text)
payload = {"word":"Python","meaning":"Reptile"}
#requests.post(url,data=payload)
#print(requests.get(url+ "/Python").text)
#payload = {"word":"Python","meaning":"A popular language"}
#requests.put(url,data=payload)
#print(requests.get(url+ "/Python").text)
payload = {"word":"Python"}
requests.delete(url,data=payload)
print(requests.get(url+ "/Python").text)
"""




"""
