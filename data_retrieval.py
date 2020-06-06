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
        posts_db = establish_connection("persistence.sqlite")

    return posts_db


def access_accounts():
    global accounts_db
    if accounts_db is None:
        accounts_db = establish_connection("./login/users.db")

    return accounts_db




# POST DATA


def get_user_posts(user_id):
	posts = query(access_posts(), "SELECT postid, post, timestamp, resolved FROM User_Posts WHERE userid=?", (user_id,))
	return posts


def add_user_post(user_id, post):
	timestamp = dt.datetime.now()
	query(access_posts(), "INSERT INTO User_Posts (userid, post, timestamp, resolved) VALUES (?, ?, ?, ?)", (user_id, post, timestamp.strftime('%m-%d-%Y %H:%M:%S'), 0))
	return


def get_expired_posts(user_id):
	posts = get_user_posts(user_id)
	results = []
	for post in posts:
		if dt.datetime.strptime(post[2], '%m-%d-%Y %H:%M:%S') < (dt.datetime.now() - WAITING_PERIOD) and int(post[3])==0:
			results.append(post)
	return results


def get_resolved_posts(user_id):
	return query(access_posts(), "SELECT * FROM User_Posts WHERE resolved=1 AND userid=?", (user_id, ))


def delete_post(post_id):
	query(access_posts(), "DELETE FROM User_Posts WHERE postid=?", (post_id,))
	return


def resolve_post(post_id):
	query(access_posts(), "UPDATE User_Posts SET resolved=1 WHERE postid=?", (post_id,))
	return


def get_post(post_id):
	return query(access_posts(), "SELECT userid, post, timestamp, resolved FROM User_Posts WHERE postid=?", (post_id, ))
	

def get_post_content(post_id):
	return get_post(post_id)[0][1];


def modify_post(post_id, new_post):
	query(access_posts(), "UPDATE User_Posts SET post=? WHERE postid=?", (new_post, post_id))
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
"""


# ACCOUNT DATA

def provider_id_to_user_id(provider_id):
	return query(access_accounts(), "SELECT user_id FROM flask_dance_oauth WHERE provider_user_id=?", (provider_id,))



