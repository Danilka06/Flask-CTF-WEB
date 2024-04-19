from app import app
from flask import render_template, request, jsonify
import json


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


@app.route('/api/check', methods=["GET", "POST"])
def api_check():
    if request.method == "POST":
        referrer = request.referrer
        json_data = request.json
        print(referrer, json_data)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


