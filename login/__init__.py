import os

from flask import Flask, redirect, url_for, flash, render_template
from flask_login import login_required, logout_user, current_user
from .config import Config
from .oauth import blueprint, db, login_manager

print(os.getcwd())

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(blueprint, url_prefix="/login")
db.init_app(app)
login_manager.init_app(app)


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You have logged out")
    return redirect(url_for("index"))


@app.route("/", methods=['GET', 'POST'])
def index():

    if not current_user.is_anonymous:
        return '<a href="/logout">Log out</a>'
    else:
        return '<a href="/login/twitter">Log in</a>'

    #return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)
