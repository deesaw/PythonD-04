#Exception with finally clause
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
print("done")
#finally is executed in any event        