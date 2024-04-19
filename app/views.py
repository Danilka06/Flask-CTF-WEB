from app import app
from flask import render_template, request, jsonify
import json

from app.api_check import *

with open('app/config.json', 'r') as file:
    CONFIG = json.load(file)

URL = CONFIG['url']


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", url=URL)


@app.route('/tasks/1')
def page_task1():
    return render_template("task1.html", url=URL)


@app.route('/tasks/2')
def page_task2():
    return render_template("task2.html", url=URL)


@app.route('/tasks/3')
def page_task3():
    return render_template("task3.html", url=URL)


@app.route('/tasks')
def page_tasks():
    return render_template("tasks.html", url=URL)


@app.route('/about')
def page_about():
    return render_template("about.html", url=URL)


@app.route('/contact')
def page_contact():
    return render_template("contact.html", url=URL)


@app.route('/api/check', methods=["GET", "POST"])
def page_api_check():
    if request.method == "POST":
        check = api_check(request.referrer, request.json, CONFIG)
        referrer = request.referrer
        json_data = request.json
        print(referrer, json_data)
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


