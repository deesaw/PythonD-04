def division():
    x = 1/0

try:
    division()
except ZeroDivisionError as err:
    print('Check your denominator.\n The system generated error is', err)


