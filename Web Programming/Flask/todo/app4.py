from flask import Flask,request,redirect,url_for ,render_template
import sqlite3
import dbTasks
app=Flask(__name__)
@app.route("/")
def addTask():
    task1=[]
    connection = sqlite3.connect('taskdb.db')
    cursor = connection.cursor()
    sql=cursor.execute('select * from mytask')
    for s in sql:
        print("########",s[0])
        
    #print("********",tasks.tid)
    return render_template('home.html',s=s)
if __name__=='__main__':
    
    app.run(debug=True)
