from flask import Flask, render_template, request
from helpers import *
from data_retrieval import *
from login.__init__ import *
import sqlite3
import tweepy


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

def postTweet(tweet):
    connection = sqlite3.connect("login/users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT token FROM flask_dance_oauth WHERE id="+current_user.get_id()+";")
    x = json.loads(cursor.fetchone()[0])
    auth = tweepy.OAuthHandler(Config.TWITTER_OAUTH_CLIENT_KEY, Config.TWITTER_OAUTH_CLIENT_SECRET)
    auth.set_access_token(x["oauth_token"], x["oauth_token_secret"])
    api = tweepy.API(auth)
    api.update_status(tweet)

if __name__ == '__main__':
    app.run(debug=True)
