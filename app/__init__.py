import os

from flask import Flask
from flask_login import LoginManager
from app.core import db_session
from app.core import queries

db_session.global_init(f"sqlite:////{os.getcwd()}/app/data/db.db")

app = Flask(__name__)
app.config["SECRET_KEY"] = "amogus1337"

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def loader_user(user_id):
    return queries.get_user_by_id(user_id)


from app import views
