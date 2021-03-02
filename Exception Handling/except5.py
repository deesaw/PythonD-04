while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError as err:
        
        print("Not a valid Input:\nThe system reported error is : ",err)
