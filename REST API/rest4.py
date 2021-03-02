import requests
url = "http://garuda.pythonanywhere.com/words"
response = requests.get(url+ "/water")
if response.ok:
    print(response.text)
else:
    print("there was an error")
