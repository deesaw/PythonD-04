import sys
import requests
import os
url="http://garuda.pythonanywhere.com/uploader"

if len(sys.argv) == 2:
	file2upload=sys.argv[1]
else:
	file2upload=input("File to upload:")
myfile = open(file2upload,'rb')


r=requests.post(url,files={'file':myfile})
if r.ok:
	print("Successfully uploaded {} bytes".format(os.path.getsize(file2upload)))
else:
	print("Sorry could not upload")

