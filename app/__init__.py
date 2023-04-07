# app/__init__.py
from flask import Flask
from config import Config
from flask_session import Session


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    Session(app)

    with app.app_context():
        from app import routes

    return app


app = create_app()
