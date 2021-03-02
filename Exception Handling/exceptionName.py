#prints the exception name 
try:
    a=10/0
except Exception as ex:
    raise Exception("Invalid Level")
    
    print("prints the exception name:",type(ex).__name__)
    print("Prints the arguments",e)
def func(level):
    if level < 1:
        raise Exception("Invalid level")
func(0)

 
