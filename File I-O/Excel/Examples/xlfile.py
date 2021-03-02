 #creating an excel file

import xlwt

wb = xlwt.Workbook()                #creates excel workbook 'wb'
ws = wb.add_sheet("Cities")         #creates excel worksheet 'ws' in 'wb'

ws.write(0,0,"Hyderabad")           #writes in first cell
ws.write(0,1,"City of Pearls")      #first row, second column

ws.write(1,0,"Jaipur")              #second row, first column
ws.write(1,1,"Pink City")           #second row, second column

ws.write(2,0,"Bangalore")           #third row, first column
ws.write(2,1,"Garden City")         #third row, second column

wb.save("cities1.xls")               #saves 'wb' as 'cities.xls'
