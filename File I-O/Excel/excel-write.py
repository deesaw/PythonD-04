import xlwt
wb = xlwt.Workbook()
ws = wb.add_sheet('A Test Sheet')

ws.write(0, 0, 'Test')
ws.write(2, 0, 99)
ws.write(2, 1, 199)

wb.save('example.xls')
