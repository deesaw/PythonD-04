import re
ss='test hello TEST'
print(re.findall('TeSt',ss,re.IGNORECASE))

name_check = re.compile(r"[^A-Z]",re.IGNORECASE)

name = input ("Please, enter your name: ")

while name_check.search(name):
    print ("Please enter your name correctly!")
    name = input ("Please, enter your name: ")





