import xlrd
def open_file(path):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)
    print book.nsheets					# print number of sheets
    print book.sheet_names()			# print sheet names
    first_sheet = book.sheet_by_index(0)# get the first worksheet
    print first_sheet.row_values(0)		# read a row
    cell = first_sheet.cell(0,0)		# read a cell
    print cell
    print cell.value
    print first_sheet.row_slice(rowx=0,start_colx=0,end_colx=2) # read a row slice
if __name__ == "__main__":
    path = "test.xls"
    open_file(path)