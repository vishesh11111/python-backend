# app/__init__.py
from flask import Flask
from app.controllers.user_controller import user_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_bp)
    return app
