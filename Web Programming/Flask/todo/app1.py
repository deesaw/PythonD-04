from flask import Flask,request,redirect,url_for 
import sqlite3
import datetime,os
app=Flask(__name__)
@app.route("/listtask")
def listtask():
    output = "<table border=1>"
    conn = sqlite3.connect("taskdb1.db")
    cursor = conn.cursor()
    row = '''<tr><td>{}</td>
            <td><a href="/remove/{}">X</a></td>
            <td><a href="/edit/{}">Modify</a></td></tr>
           '''
    for new_task in cursor.execute('SELECT * from task'):
        output+=row.format(new_task,new_task,new_task)
    output+="</table>"
    conn.close()
    
    return output
        
@app.route('/')
def homePage():
    
    html= '''
    
    <h1>Welcome to To-Do list</h1><br>
    <br><p style="font-size:160%;"><a href="http://localhost:5000/addTask">Add New Task</a></p></br>
    <p style="font-size:160%;">List Tasks</p><br>
    '''
    return html
    
@app.route('/addTask')
def addTask():
    return '''
    
    <h1>Add New Task</h1><br>
    <form action='/addNewTask' method=post>
    <input type='checkbox' name=cb >
    <input type = text name=new_task>
    #<br><input type=submit>
    </form>
    '''
#
@app.route('/addNewTask',methods=["POST"])
def addNewTask():
    print('********************......')
    new_task=request.form.get("new_task")
    print('********************')
    print("NNNNNNNNNNNNNNNNNNN",new_task)
    #insert values in to database
    conn = sqlite3.connect("taskdb1.db")
    cursor = conn.cursor()
    # insert some data
    sql = "INSERT INTO task VALUES ('{}')".format(new_task)
    
    cursor.execute(sql)
    # save data to database
    conn.commit()
    conn.close()
    return redirect(url_for("listtask"))
@app.route("/remove/<new_task>")
def remove(new_task):
    conn = sqlite3.connect("taskdb1.db")
    cursor = conn.cursor()
    print("%%%%%%%%%%%%%%%%%%%",new_task)
   
    sql = """DELETE FROM task
    WHERE new_task = {}""".format(new_task)
    cursor.execute(sql)
    # save data to database
    conn.commit()
    conn.close()
    return redirect(url_for("listtask"))
    
if __name__=='__main__':
    
    app.run(debug=True)
