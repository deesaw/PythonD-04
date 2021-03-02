#Custom class
class Custom_error(BaseException):
    pass

try:
    print("hello")
    raise Custom_error
    print("world")
except Custom_error:
    print("found it not stopping now")

print("im outside")
try:
    a = int(input("Enter a positive integer value: "))
    if a <= 0:
        raise ValueError("This is not a positive number!!")
except ValueError as ve:
    print(ve)
