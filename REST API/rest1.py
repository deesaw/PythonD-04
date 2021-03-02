import requests
url = "http://api.open-notify.org/iss-now.json"
response =  requests.get(url)
output = response.json()
#print(type(output))
lat = output.get("iss_position").get("latitude")
longi = output.get("iss_position").get("longitude")
print("ISS is currently at {},{}".format(lat,longi))
