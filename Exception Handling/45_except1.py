while True:
    try:
        x = int(input("Please enter a number: "))
        print("Entered number is ", x)
        break
    except ValueError:
        print("Oops!  That was not a valid number.  Try again...")
