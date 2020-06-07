from flask import Flask, render_template, request, jsonify
from flask_login import login_required, logout_user, current_user
from helpers import *
from data_retrieval import *
from login.__init__ import *

app = Flask('PreTweet', static_url_path='/')
init_login(app)

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
       	return render_template('app.html')
    else:
        return render_template('templates/index.html')

@app.route("/posts", methods=['GET', 'PUT'])
@login_required
def posts():
    if request.method == 'GET':
        # return all pending posts
        posts = get_user_posts(current_user.get_id())
        response = []
        for post in posts:
            response.append(post_to_json(post[0]))
        return jsonify(response), 200

    if request.method == 'PUT':
        # add a partial post to database
        post = add_user_post(current_user.get_id(), request.get_json()['content'], request.get_json()['time'])
        return post_to_json(post[0][0]), 200
    
    return "{}", 200

@app.route('/posts/<id>', methods=['DELETE'])
@login_required
def posts_delete(id):
    delete_post(id)
    return '{}', 200


@app.route("/request-review", methods=['POST'])
@login_required
def request_review():
    if(request.method == 'POST'):
        request_post_review(request.get_json()['id'])
        return "{}", 200
    
    return "{}", 200


@app.route("/tweet", methods=['POST'])
@login_required
def tweet():
    if(request.method == 'POST'):
        postTweet(current_user.get_id(), request.get_json()['id'])
        return "{}", 200
    
    return "{}", 200

if __name__ == '__main__':
    app.run(debug=True)
