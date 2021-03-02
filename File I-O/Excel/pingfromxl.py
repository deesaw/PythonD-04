import xlrd
import os
wb = xlrd.open_workbook("ips.xls")
ws = wb.sheet_by_name("ips")
for row in range(ws.nrows):
	ip = ws.cell(row,0).value

	pingstring = "ping {} >NUL".format(ip)
	response = os.system(pingstring)
	if response == 0:
		print("{} is up".format(ip))
	else:
		print("{} is down".format(ip))
