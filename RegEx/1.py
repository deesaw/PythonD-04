import re
# Regular expression to replace pin value to * where ever it is located
mob="My mobile number is 9888080808,  8900 and my pin is 7890"

nn=re.sub(r"\b\d{4}\b","****",mob)
print("Pin: ",nn)
