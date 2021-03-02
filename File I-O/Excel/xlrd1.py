#Excel reading

import xlrd                             #imports xlrd module

wb = xlrd.open_workbook("cities1.xls")   #opens 'cities1.xlsx' into 'wb'

print (wb.nsheets)                      #prints number of sheets in 'wb'
print (wb.sheet_names())                #prints sheet_names

ws = wb.sheet_by_name("Cities")

print (ws.nrows)
print (ws.ncols)

print (ws.cell(0,0))

#print (ws.col(1))

#print (ws.row(3))

#print (ws.cell(3,2))
