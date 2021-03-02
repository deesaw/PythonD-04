from flask import Flask,request,redirect,url_for 
import sqlite3
import datetime,os
app=Flask(__name__)
@app.route("/")
def addTask():    
    html="""
    <div>Add a new ToDo item:
        <form action='/addnewtask' method="POST">
            <tr> <td> <input type=text name=task> <td>
            <input type="submit" value="Add New Task"><br>

        </form>
    </div>
    """
    html+="<table border=1>"
    conn = sqlite3.connect("taskdb.db")
    cursor = conn.cursor()
    
    for tid,newTask,done in cursor.execute("SELECT tid,task,done FROM mytask"):
        
        row = '<tr>'
        if done=='True':
             row+='<td><strike><font color="grey">{}</strike></font></td>'
        else:
            row+='<td>{}</td>'
        row+="""<td><a href="/remove/{}">X</a></td>
                 <td><a href="/edit/{}">Done</a></td></tr>
                 """
            
        html+=row.format(newTask,tid,tid)
    conn.close()
    html+="</table>"
    
    return html

    
@app.route("/addnewtask",methods=['POST'])
def addnewtask():
    task=request.form.get("task")
    conn = sqlite3.connect("taskdb.db")
    cursor = conn.cursor()
    sql = "INSERT INTO mytask (task) VALUES ('{}')".format(task)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
    return redirect(url_for("addTask"))

@app.route("/remove/<tid>")
def remove(tid):
    conn = sqlite3.connect("taskdb.db")
    cursor = conn.cursor()
    sql = """DELETE FROM mytask
    WHERE tid = {}""".format(tid)
    cursor.execute(sql)
    # save data to database
    conn.commit()
    conn.close()
    return redirect(url_for("addTask"))
@app.route("/edit/<tid>")
def edit(tid):
    conn = sqlite3.connect("taskdb.db")
    cursor = conn.cursor()
    sql="UPDATE mytask SET done='{}' where tid={}".format(True,tid)
    cursor.execute(sql)
    conn.commit()
    conn.close()
    return redirect(url_for("addTask"))
    
    
    
if __name__=='__main__':
    
    app.run(debug=True)

