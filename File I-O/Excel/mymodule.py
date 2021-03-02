import os
import xlrd
def myping(ip):
	pingstring = "ping -c2 {} >/dev/null".format(ip)
	response = os.system(pingstring)
	if response == 0:
		print("{} is up".format(ip))
	else:
		print("{} is down".format(ip))

def get_ips_from_xl(workbook):
	wb = xlrd.open_workbook(workbook)
	ws = wb.sheet_by_index(0)
	return ws.col_values(0)
