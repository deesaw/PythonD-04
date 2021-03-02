import sqlite3
conn=sqlite3.connect("ips.db")
mycursor=conn.cursor()

sql=""" CREATE TABLE ips
                (sno INTEGER PRIMARY KEY,
                ip TEXT,
                status TEXT)"""
mycursor.execute(sql)

conn.close()
