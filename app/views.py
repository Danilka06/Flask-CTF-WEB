from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/tasks/1')
def task1():
    return render_template("task1.html")


@app.route('/tasks/2')
def task2():
    return render_template("task2.html")


@app.route('/tasks/3')
def task3():
    return render_template("task3.html")


@app.route('/tasks')
def tasks():
    return render_template("tasks.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact')
def contact():
    return render_template("contact.html")



