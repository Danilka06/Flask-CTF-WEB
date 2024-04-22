import json

from flask import render_template, request

from app import app
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


@app.route('/robots.txt')
def page_robots():
    f = open("app/robots.txt", 'r')
    data = f.read()
    f.close()
    return data


@app.route('/shit_happens')
def page_shit_happens():
    return render_template("shit_happens.html", url=URL)


@app.route('/api/check', methods=["GET", "POST"])
def page_api_check():
    codes = {
        200: "correct",
        300: "incorrect",
        400: "error"
    }
    status = "error"
    if request.method == "POST":
        check = api_check(request.referrer, request.json, CONFIG)
        status = codes[check]

    return json.dumps({'status': status}), 200, {'ContentType': 'application/json'}


@app.route('/amogus')
def page_amogus():
    return CONFIG["tasks"]['2']['answer']


@app.route('/login')
def page_login():

    return render_template('login.html', url=URL)


@app.route('/signup')
def page_signup():
    return render_template('signup.html', url=URL)

