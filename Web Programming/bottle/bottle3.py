from bottle import run,route
import time
@route("/")
def hello():
	return "Hi from bottle"

@route("/contact")
def hello1():
	return "Contact Ramesh at 9885970033"

@route("/now")
def abcd():
	return str(time.ctime(time.time()))
@route("/ipsall")
def ipsall():
	import sqlite3 #don't do this in real life
	conn=sqlite3.connect("ips.db")
	cursor=conn.cursor()
	ips = cursor.execute("select * from ips").fetchall()
	conn.close()
	return str(ips)
@route("/ipsallhtml")
def ipsallhtml():
	import sqlite3 #don't do this in real life
	conn=sqlite3.connect("ips.db")
	cursor=conn.cursor()
	ips = cursor.execute("select * from ips").fetchall()
	conn.close()
	output = "<table border=1>"
	row = "<tr><td>{}</td><td>{}</td><td>{}</td></tr>"
	for sno,ip,status in ips:
		output+=row.format(sno,ip,status)
	output+="</table>"
	return output
run()




