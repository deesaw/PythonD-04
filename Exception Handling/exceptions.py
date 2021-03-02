#Exceptions


while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")


		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError as err:
    print 'Check your denominator.\n The system generated error is', err


	
	
	


def divide(y):
    x = 1/y

try:
    divide(2)
finally:
    print "done"

try:
    divide(0)
finally:
    print "done"
    
	
	
	




    try:
        x = int(raw_input("Please enter a number: "))
        
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    else:
        print "That was a valid input"


		
		
		
		
while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError as err:
        
        print("No a valid Input:\nThe system reported error is : ",err)

		
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
	else:
        print("result is", result)
    finally:
        print("executing finally clause")
divide(2, 1)
divide(2, 0)
divide('a','b')
print "done"
#finally is executed in any event        




Raising a custom exception

try:
   raise Exception('myExcetionType', 'myArgument')
except Exception as inst:
   print(type(inst))    # the exception instance
   print(inst.args)     # arguments stored in .args
   print(inst)          # __str__ allows args to be printed directly,
                        # but may be overridden in exception subclasses
   x, y = inst.args     # unpack args
   print('x =', x)
   print('y =', y)

   
   
   
   


   
overheat=Exception('OverHeatException','Please check water in the radiator')

print type(overheat)  
   
def gettemp():
    import random
    return random.randint(1,4500)
   
while True:
	currenttemp=gettemp()
    if currenttemp<4490:
		print "keep driving",currenttemp
    else:
		raise overheat
		
		
		
		
		
		
		
		
		
def fact(n):
    if n < 0:
        raise ValueError("negative numbers do not have factorials")
    f=1
    for x in range(2,n+1):
        f*=x
    return  f

print(fact(10))
print(fact(0))
print(fact(-10))



