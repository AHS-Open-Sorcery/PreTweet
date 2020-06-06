import sqlite3
from sqlite3 import Error
import datetime as dt
from datetime import *
import time


def establish_connection(file):
	try: 
		connection = sqlite3.connect(file)
		return connection
	except Error as e:
		print(e)
	
	return None


def query(connection, command, parameters):
	cursor = connection.cursor()
	cursor.execute(command, parameters)
	results = cursor.fetchall()
	cursor.close()
	connection.commit()
	return results

posts_db = None
accounts_db = None
WAITING_PERIOD = timedelta(seconds=1)


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




# POST DATA

def get_user_posts(user_id):
	posts = query(access_posts(), "SELECT * FROM User_Posts WHERE userid=?", (user_id, ))
	return posts


def add_user_post(user_id, post):
	timestamp = dt.datetime.now()
	query(access_posts(), "INSERT INTO User_Posts (userid, post, timestamp, resolved) VALUES (?, ?, ?, ?)", (user_id, post, timestamp.strftime('%m-%d-%Y %H:%M:%S'), 0))
	return


def get_expired_posts(user_id):
	posts = get_user_posts(user_id)
	results = []
	for post in posts:
		if dt.datetime.strptime(post[3], '%m-%d-%Y %H:%M:%S') < (dt.datetime.now() - WAITING_PERIOD) and int(post[4])==0:
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




# ACCOUNT DATA

def set_email(user_id, email):
	query(access_users(), "UPDATE user SET email=? WHERE id=?", (email, user_id))
	return


def get_email(user_id):
	return query(access_accounts(), "SELECT email FROM user WHERE id=?", (user_id, ))


def get_all_users():
	return query(access_accounts(), "SELECT DISTINCT id FROM user", ())




# REVIEW DATA

"""
status: 'NOT_STARTED'	0
status: 'IN_PROGRESS'	1
status: 'COMPLETE'		2
"""

def get_reviews(post_id):
	return query(access_posts(), "SELECT * FROM Reviews WHERE postid=?", (post_id, ))


def add_review(reviewer, post_id, comment):
	timestamp = dt.datetime.now()
	query(access_posts(), "INSERT INTO Reviews (reviewerid, postid, comment, timestamp, status) VALUES (?, ?, ?, ?, ?)", 
		(reviewer, post_id, comment, timestamp.strftime('%m-%d-%Y %H:%M:%S'), 0))
	return


def set_review_status(review_id, status):
	query(access_posts(), "UPDATE Reviews SET status=? WHERE reviewid=?", (status, review_id))
	return



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

