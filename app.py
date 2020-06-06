from flask import Flask, render_template, request, jsonify
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
       	user_id = current_user.get_id()
       	add_user_post(user_id, "This is a post")
       	login_manager.login_view = 'index'
       	return '<a href="/logout">Log out</a>', 200
    else:
        return '<a href="/login/twitter">Log in</a>', 200

@app.route("/posts", methods=['GET', 'PUT', 'DELETE'])
def posts():
    if request.methods == 'GET':
        # return all pending posts
        posts = get_unresolved_posts(current_user.get_id())
        request = []
        for post in posts:
            request.append(post_to_json(post))
        return jsonify(request), 200

    if request.methods == 'PUT':
        # add a partial post to database
        post = add_user_post(current_user.getid(), request.json['content'], request.json['time'])
        return post_to_json(post), 200
    
    if request.methods == 'DELETE':
        delete_post(request.json['post_id'])
        return "", 200
    
    return "", 200


@app.route("/request-review", methods=['POST'])
def request_review():
    if(request.method == 'POST'):
        request_post_review(request.json['post_id'])
        return "", 200
    
    return "", 200


@app.route("/tweet", methods=['POST'])
def tweet():
    if(request.method == 'POST'):
        postTweet(request.json['post_id'])
        return "", 200
    
    return "", 200




if __name__ == '__main__':
    app.run(debug=True)
