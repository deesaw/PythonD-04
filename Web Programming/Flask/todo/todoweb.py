from flask import Flask,request,redirect,url_for ,render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///taskdb.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
class Todo(db.Model):
    tid=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(200))
    complete=db.Column(db.Boolean)
    def __init__(self, text):
        self.tid=None
        self.text = text
        self.done = False
    
db.create_all()

@app.route('/')
def tasks_list():
    tasks=Todo.query.all()     
    return render_template('style.html',tasks=tasks)

@app.route('/task', methods=['POST'])
def add_task():
    content=request.form['content']
    if not content:
        return redirect('/')
    task=Todo(content)
    db.session.add(task)
    db.session.commit()
    return redirect('/')
@app.route('/deleteTask/<tid>')
def deleteTask(tid):
    task=Todo.query.get(tid)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')
@app.route('/completedTask/<tid>')
def completedTask(tid):
    task=Todo.query.get(tid)
      
    if task:
        task.complete=True

    db.session.commit()
    return redirect('/')
    
if __name__=='__main__':
    app.run(debug=True)
