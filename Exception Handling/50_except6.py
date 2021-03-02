overheat=Exception('OverHeatException','Please check water in the radiator')

print(type(overheat)) 
   
def gettemp():
    import random
    return random.randint(1,4500)
   
while True:
    currenttemp=gettemp()
    if currenttemp<4490:
            print( "keep driving",currenttemp)
    else:
        raise overheat
