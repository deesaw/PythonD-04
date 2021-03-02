#how to use bottle
from bottle import route, run, request, template
import os
import sqlite3
@route('/')
def hello():
    return "Hey I am bottle here how are you doing?"

@route('/env') #displays environment as table format
def env1():    
    output='<table border=1>'
    for x,y in os.environ.items(): #command to get the environment variables
        output=output +"<tr><td>"+ x +"</td><td>"+ y + "</td></tr>"
    return output + "</table>"

@route('/wish/<name>') #to this route we sending a dynamic name
def wish(name):
    return "Hello {} how are you doing today".format(name)
run(host='localhost', port=8080, debug=True)

@route('/cars')
def books():
    
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    output='<table border=1>'
    tablerow="<tr><td>{}</td><td>{}</td></tr>"
    sql = "SELECT * FROM cars"
    
    for id,bookname,author in cursor.execute(sql):
             output+=tablerow.format(carname,price)
    output+="</table>"
    
    conn.close()
    return output
run(host='localhost', port=8080, debug=True)


