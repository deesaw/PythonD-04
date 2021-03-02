import xlwt
f=open("ips.txt","r")#open text file
wb = xlwt.Workbook()#open xl workbook
ws = wb.add_sheet("ips")#create xl worksheet
for row,line in enumerate(f):#read line by line
	ws.write(row,0,line.strip())
f.close()#close file
wb.save("ips.xls") #save the workbook
