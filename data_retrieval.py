import sqlite3
from sqlite3 import Error
import datetime as dt
from datetime import *
import time
import helpers


def establish_connection(file):
	try: 
		connection = sqlite3.connect(file)
		return connection
	except Error as e:
		print(e)
	
	return None


posts_db = None
accounts_db = None
WAITING_PERIOD = timedelta(seconds=10)


def access_posts():
    global posts_db
    if posts_db is None:
        posts_db = establish_connection("posts.db")

    return posts_db


def access_accounts():
    global accounts_db
    if accounts_db is None:
        accounts_db = establish_connection("./login/users.db")

    return accounts_db


def close_connections():
	global posts_db, accounts_db
	if posts_db is not None:
		posts_db.close()
		posts_db = None
	if accounts_db is not None:
		accounts_db.close()
		accounts_db = None


def query(connection, command, parameters):
	cursor = connection.cursor()
	cursor.execute(command, parameters)
	results = cursor.fetchall()
	cursor.close()
	connection.commit()
	close_connections()
	return results


# POST DATA

def get_user_posts(user_id):
	posts = query(access_posts(), "SELECT * FROM User_Posts WHERE userid=?", (user_id, ))
	return posts


def add_user_post(user_id, post, timestamp = None):
	if(timestamp is None):
		timestamp = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	else: # time is in milliseconds
		timestamp = helpers.ms_to_time(timestamp)
	query(access_posts(), "INSERT INTO User_Posts (userid, post, timestamp, resolved, needs_review) VALUES (?, ?, ?, ?, ?)", 
		(user_id, post, timestamp, 0, 0))
	return query(access_posts(), "SELECT * FROM User_Posts WHERE userid=? AND post=? AND timestamp=?", (user_id, post, timestamp))


def get_expired_posts(user_id):
	posts = get_user_posts(user_id)
	results = []
	for post in posts:
		if dt.datetime.strptime(post[3], '%Y-%m-%d %H:%M:%S') < (dt.datetime.now() - WAITING_PERIOD) and int(post[4])==0:
			results.append(post)
	return results


def get_resolved_posts(user_id):
	return query(access_posts(), "SELECT * FROM User_Posts WHERE resolved=1 AND userid=?", (user_id, ))


def get_unresolved_posts(user_id):
	return query(access_posts(), "SELECT * FROM User_Posts WHERE resolved=0 AND userid=?", (user_id, ))


def delete_post(post_id):
	query(access_posts(), "DELETE FROM User_Posts WHERE postid=?", (post_id, ))
	return


def resolve_post(post_id):
	query(access_posts(), "UPDATE User_Posts SET resolved=1 WHERE postid=?", (post_id, ))
	return


def get_post(post_id):
	return query(access_posts(), "SELECT * FROM User_Posts WHERE postid=?", (post_id, ))
	

def get_post_content(post_id):
	return get_post(post_id)[0][2]; # 2 should be the index of the post content


def modify_post(post_id, new_post):
	query(access_posts(), "UPDATE User_Posts SET post=? WHERE postid=?", (new_post, post_id))
	return


def request_post_review(post_id):
	query(access_posts(), "UPDATE User_Posts SET needs_review=1 WHERE postid=?", (post_id, ))
	return



# ACCOUNT DATA

def set_email(user_id, email):
	query(access_accounts(), "UPDATE user SET email=? WHERE id=?", (email, user_id))
	return


def get_email(user_id):
	return query(access_accounts(), "SELECT email FROM user WHERE id=?", (user_id, ))


def get_all_users():
	return query(access_accounts(), "SELECT DISTINCT id FROM user", ())





# REVIEW DATA

"""
status: 'NOT_STARTED'	0
status: 'PENDING'		1
status: 'COMPLETE'		2
"""
REVIEW_STATUS_LIST = ['NOT_STARTED', 'PENDING', 'COMPLETE']

def get_reviews(post_id):
	return query(access_posts(), "SELECT * FROM Reviews WHERE postid=?", (post_id, ))


def add_review(reviewer, post_id, comment):
	timestamp = dt.datetime.now()
	query(access_posts(), "INSERT INTO Reviews (reviewerid, postid, comment, timestamp, status) VALUES (?, ?, ?, ?, ?)", 
		(reviewer, post_id, comment, timestamp.strftime('%Y-%m-%d %H:%M:%S'), 0))
	return


def set_review_status(review_id, status):
	query(access_posts(), "UPDATE Reviews SET status=? WHERE reviewid=?", (status, review_id))
	return



# TO JSON

def review_to_json(review_id):
	 # there should only be one review with this id
	data = query(access_posts(), "SELECT * FROM Reviews WHERE reviewid=?", (review_id, ))
	timestamp = helpers.time_to_ms(dt.datetime.strptime(data[0][4], '%Y-%m-%d %H:%M:%S'))
	review = {"id": review_id, "reviewerId": data[0][2], "time": timestamp, "comments": data[0][3]}
	return review


def post_to_json(post_id):
	 # there should only be one review with this id
	data = query(access_posts(), "SELECT * FROM User_Posts WHERE postid=?", (post_id, ))
	reviews = []
	min_status = 3
	max_status = -1

	for review in get_reviews(post_id):
		reviews.append(review_to_json(review[0]))
		status = review[5]
		min_status = min(min_status, status)
		max_status = max(max_status, status)
		print(status)
	
	review_status_num = 0 if min_status == 3  else min_status if min_status == max_status else 1
	post_time = dt.datetime.strptime(data[0][3].split('.')[0] + ' UTC', '%Y-%m-%d %H:%M:%S %Z')

	post = {"id": post_id, "sentiment": helpers.getSentimentPolarity(data[0][2]), 
		"delay": WAITING_PERIOD.total_seconds(), 
		"resolved": data[0][4], "reviewStatus": REVIEW_STATUS_LIST[review_status_num], "reviews": reviews,
		"content": data[0][2], "time": post_time.timestamp() * 1000 }
	return post


"""
#Testing Code:

add_user_post(1, "hi")
add_user_post(2, "High")
add_user_post(2, "bye")
add_user_post(1, "Bye")

print(get_user_posts(1))
print(get_user_posts(2))

time.sleep(3)

add_user_post(1, "hey")
add_user_post(2, "hay")

print(get_user_posts(1))
print(get_user_posts(2))
print(get_expired_posts(1))
print(get_expired_posts(2))

delete_post(1)
resolve_post(2)

print(get_expired_posts(1))
print(get_expired_posts(2))
print(get_resolved_posts(1))
print(get_resolved_posts(2))



add_review(2, 2, "Nice")
add_review(1, 2, "I know")
add_review(2, 3, "Nice2")
add_review(1, 3, "Nice3")

print(get_reviews(2))
print(get_reviews(3))
"""

