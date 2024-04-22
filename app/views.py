import json

from flask import render_template, request, jsonify
from flask_login import login_required, login_user

from app import app
from app.api_check import *
from app.core.models import User
from app.core import queries

with open('app/config.json', 'r') as file:
    CONFIG = json.load(file)

URL = CONFIG['url']


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", url=URL)


@app.route('/tasks/1')
@login_required
def page_task1():
    return render_template("task1.html", url=URL)


@app.route('/tasks/2')
@login_required
def page_task2():
    return render_template("task2.html", url=URL)


@app.route('/tasks/3')
@login_required
def page_task3():
    return render_template("task3.html", url=URL)


@app.route('/tasks')
@login_required
def page_tasks():
    return render_template("tasks.html", url=URL)


@app.route('/about')
def page_about():
    return render_template("about.html", url=URL)


@app.route('/contact')
def page_contact():
    return render_template("contact.html", url=URL)


@app.route('/robots.txt')
@login_required
def page_robots():
    f = open("app/robots.txt", 'r')
    data = f.read()
    f.close()
    return data


@app.route('/shit_happens')
@login_required
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


@app.route('/api/login', methods=["POST"])
def page_api_login():
    data = request.json
    login = data["login"]
    password = data["password"]
    if (user := queries.get_user_by_login(login)) is None:
        print(user)
        print('no user')
        return jsonify({"status": "error"}), 300
    if not (queries.get_password_by_login(login).check_password(password)):
        print('incorrect password')
        return jsonify({"status": "error"}), 301
    print('all correct')
    print(request.json)

    login_user(user, remember=True)

    return json.dumps({'status': "ok"}), 200, {'ContentType': 'application/json'}


@app.route('/amogus')
@login_required
def page_amogus():
    return CONFIG["tasks"]['2']['answer']


@app.route('/login')
def page_login():
    return render_template('login.html', url=URL)


@app.route('/signup')
def page_signup():
    return render_template('signup.html', url=URL)


@app.route('/api/signup', methods=["POST"])
def page_api_signup():
    data = request.json
    login = data["login"]
    password = data["password"]

    if queries.get_user_by_login(login):
        return json.dumps({'status': "login is used"}), 300, {'ContentType': 'application/json'}

    user = User()
    user.login = login
    user.set_password(password)

    queries.add_and_commit(user)

    login_user(user)
    return json.dumps({'status': "ok"}), 200, {'ContentType': 'application/json'}


