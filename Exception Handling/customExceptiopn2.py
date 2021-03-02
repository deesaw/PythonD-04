#define Python user-defined exceptions
'''
A custom exception is one which the programmer creates himself.
This is done by adding a new class.
derive the custom exception class from the base exception class.
'''
class Error(Exception):
   """Base class for other exceptions"""
   pass
 
class InputTooSmallError(Error):
   """Raised when the entered number is smaller than the actual one"""
   pass
 
class InputTooLargeError(Error):
   """Raised when the entered number is larger than the actual one"""
   pass

number = 27
 
while True:
   try:
       apb =  int(input("Enter a number: "))
       if apb < number:
           raise InputTooSmallError
       elif apb > number:
           raise InputTooLargeError
       break
   except InputTooSmallError:
       print("The entered number is too small, try again!")
       print('')
   except InputTooLargeError:
       print("The entered number is too large, try again!")
       print('')
 
print("Congratulations! You guessed it correctly.")
