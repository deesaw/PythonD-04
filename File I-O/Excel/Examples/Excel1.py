import xlrd
wb = xlrd.open_workbook("Marks.xlsx")
print(wb.sheet_names())
print(wb.nsheets)
ws = wb.sheet_by_index(0)
print(ws.nrows)
print(ws.ncols)
print(ws.cell(0,3).value)
