from flask import Flask, render_template, request
from helpers import *
from dataRetrieval import *
from login.__init__ import *



@app.route("/", methods=['GET', 'POST'])
def index():

    if not current_user.is_anonymous:
       	print(current_user.get_id())
       	user_id = current_user.get_id()
       	add_user_post(user_id, "This is a post")
       	return '<a href="/logout">Log out</a>'
    else:
        return '<a href="/login/twitter">Log in</a>'


if __name__ == '__main__':
    app.run(debug=True)
