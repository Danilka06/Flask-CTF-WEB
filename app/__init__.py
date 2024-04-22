import os

from flask import Flask
from app.core import db_session

print(os.getcwd())
db_session.global_init(f"sqlite:////{os.getcwd()}/app/data/db.db")



app = Flask(__name__)
from app import views