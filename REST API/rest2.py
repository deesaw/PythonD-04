import requests
url = "http://api.open-notify.org/iss-now.json"
response =  requests.get(url)
output = response.json()
#print(type(output))
lat = output.get("iss_position").get("latitude")
longi = output.get("iss_position").get("longitude")
print("ISS is currently at {},{}".format(lat,longi))

url2="https://maps.googleapis.com/maps/api/geocode/json"
payload={"latlng":lat+","+longi}
response =  requests.get(url2,params=payload)
output = response.text
print(output)
