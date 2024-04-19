from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/tasks/<string:task_id>')
def task(task_id: str):
    print(task_id)
    return render_template(f"tasks{task_id}.html")


@app.route('/tasks')
def tasks():
    return render_template("tasks.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")



