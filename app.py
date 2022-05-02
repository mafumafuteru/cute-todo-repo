from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'your secret key'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    urgency = db.Column(db.INT, nullable=False)
    fun = db.Column(db.INT, nullable=False)
    priority = db.Column(db.INT, nullable=False)
    completed = db.Column(db.BOOLEAN, default=False)
    finish_later = db.Column(db.BOOLEAN, default=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        task_urgency = request.form['urgency-slider']
        task_fun = request.form['fun-level-slider']
        task_priority = int(request.form['fun-level-slider']) + int(request.form['urgency-slider'])
        task_content = request.form['content']
        new_task = Todo(content=task_content, priority=task_priority, urgency=task_urgency, fun=task_fun)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/viewer')
        except:
            return 'Error adding task'
    else:
        #task = Todo.query.order_by(Todo.date_created).first()
        return render_template('create_task.html')

@app.route('/viewer', methods=["POST", "GET"])
def viewer():
    task = Todo.query\
        .filter_by(completed=False)\
        .filter_by(finish_later=False)\
        .order_by(Todo.priority).first()

    if not task:
        tasks = Todo.query\
            .filter_by(completed=False).all()
        
        for task in tasks:
            task.finish_later = False
            
    if request.method == 'POST':
        if request.form["action"] == "SWITCH":
            task.finish_later = True
        elif request.form["action"] == "DONE":
            task.completed = True
        db.session.commit()
        return redirect('/viewer')
    else:
        return render_template('view_task.html', task=task)

@app.route('/daily')
def daily():
    completed_tasks = Todo.query.filter_by(completed=True)
    return render_template('daily.html', tasks=completed_tasks)

@app.route('/update/<int:id>', methods=["POST", "GET"])
def update(id):
    task = Todo.query.get_or_404(id)
    
    if request.method == 'POST':
        task.urgency = request.form['urgency-slider']
        task.fun = request.form['fun-level-slider']
        task.priority = int(request.form['fun-level-slider']) + int(request.form['urgency-slider'])
        task.content = request.form['content']

        try:
            db.session.commit()
            return redirect("/viewAll")
        except:
            return "Couldn't update task"
    else:
        return render_template('edit_task.html', task=task)

@app.route('/viewAll')
def viewAll():
    tasks = Todo.query\
        .filter_by(completed=False)\
        .order_by(Todo.priority).all()
    return render_template('view_all_tasks.html', tasks=tasks)

@app.route('/delete/<int:id>')
def deleteTask(id):
    task = Todo.query.get_or_404(id)

    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/viewAll')
    except:
        return "Couldn't delete task."

if __name__ == "__main__":
    app.run(debug=True, port=5001)

