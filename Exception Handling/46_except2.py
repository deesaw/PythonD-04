while True:
    try:
        x = input("Please enter a number: ")
        y = input("Please enter a number to divide: ")
        num= int(x)/int(y)
        print("Result: ",num)
        break
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")
    except ZeroDivisionError as err:
        print('Check your denominator.\n The system generated error is', err)
    
        
        
    
