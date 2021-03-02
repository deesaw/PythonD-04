from bottle import route, run, request, template
import os
import sqlite3
@route('/cars')
def cars():
    
    conn = sqlite3.connect("mydatabase.db")
    cursor = conn.cursor()
    output='<table border=1>'
    tablerow="<tr><td>{}</td><td>{}</td></tr>"
    sql = "SELECT * FROM cars"
    
    for id,carname,price in cursor.execute(sql):
             output+=tablerow.format(carname,price)
    output+="</table>"
    
    conn.close()
    return output
run(host='localhost', port=8081, debug=True)
