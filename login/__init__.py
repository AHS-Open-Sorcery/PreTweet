import os

from flask import Flask, redirect, url_for, flash, render_template
from flask_login import login_required, logout_user, current_user
from .config import Config
from .oauth import blueprint, db, login_manager

def init_login(app):
    app.config.from_object(Config)
    app.register_blueprint(blueprint, url_prefix="/login")
    db.init_app(app)
    login_manager.init_app(app)

