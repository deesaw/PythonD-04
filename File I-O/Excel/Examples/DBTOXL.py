import os
import sqlite3
import xlwt
wb = xlwt.Workbook()

ws = wb.add_sheet("Cities")
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()
row=0
col=0
sql = "SELECT * FROM cars"
for id,carname,price in cursor.execute(sql):
    print("ID ...{},carname ...{}....,price {}".format(id,carname,price))
    ws.write(0,0,id)

conn.close()

wb.save("marks1.xls")               
