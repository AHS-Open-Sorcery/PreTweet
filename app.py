from flask import Flask, render_template, request
from helpers import *
from data_retrieval import *
from login.__init__ import *


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    flash("You have logged out")
    login_manager.login_view = 'twitter.login'
    return redirect(url_for("index"))


@app.route("/", methods=['GET', 'POST'])
def index():

    if not current_user.is_anonymous:
       	print(current_user.get_id())
       	user_id = current_user.get_id()
       	add_user_post(user_id, "This is a post")
       	login_manager.login_view = 'index'
       	return '<a href="/logout">Log out</a>'
    else:
        return '<a href="/login/twitter">Log in</a>'



if __name__ == '__main__':
    app.run(debug=True)
