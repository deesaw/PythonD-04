import sqlite3
import os
conn = sqlite3.connect("ips.db")
mycursor=conn.cursor()
def isup(ip):
	pingstring="ping  {} > NUL".format(ip)
	if os.system(pingstring):
		return False
	else:
		return True

ips = mycursor.execute("select * from ips").fetchall()
mycursor.close()

for sno,ip,status in ips:
	if isup(ip):
		sql = """UPDATE ips SET status='up'
		 WHERE ip='{}'""".format(ip)
		mycursor=conn.cursor()
		mycursor.execute(sql)
		conn.commit()
		mycursor.close()
		print("Updated db. {} is up".format(ip))
	else:
		sql = """UPDATE ips SET status='down'
		 WHERE ip='{}'""".format(ip)
		mycursor=conn.cursor()
		mycursor.execute(sql)
		conn.commit()
		mycursor.close()
		print("Updated db. {} is down".format(ip))
conn.close()
