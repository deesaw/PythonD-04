import re

phone = "9866611005 # This is  mobile Number"

# Regular expression to replace pin value to * where ever it is located
mob="My mobile number is 9888080808,  and my pin is 7890"

nn=re.sub(r"\b\d{4}\b","****",mob)
print("Pin: ",nn)















nn1=re.sub("\d+","*",mob)
print("Pin: ",nn1)



# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Contact Number : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)

#should replace only when there is 3 digits else no
mob1="abc678iop980jkl1234"
nn1=re.sub(r"\d{3}\D","*",mob1)
print(nn1)
