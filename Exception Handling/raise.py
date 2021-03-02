import random,time		
a=Exception('Too hot','Too dangerous to drive')
def gettemp():
    return random.randint(10,105)
def watchtemp():
	temp=gettemp()
	if temp>99:
		raise a
	else:
		print temp

while True:
	watchtemp()
	time.sleep(1)
