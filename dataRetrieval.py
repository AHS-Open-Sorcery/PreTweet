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
	return results

conn = establish_connection("persistence.sqlite")
waiting_period = timedelta(seconds=1)



# POST DATA


def get_user_posts(user_id):
	posts = query(conn, "SELECT postid, post, timestamp, resolved FROM User_Posts WHERE userid=?", (user_id,))
	return posts


def add_user_post(user_id, post):
	timestamp = dt.datetime.now()
	query(conn, "INSERT INTO User_Posts (userid, post, timestamp, resolved) VALUES (?, ?, ?, ?)", (user_id, post, timestamp.strftime('%m-%d-%Y %H:%M:%S'), 0))
	return


def get_expired_posts(user_id):
	posts = get_user_posts(user_id)
	results = []
	for post in posts:
		#print(str(post) + " " + (dt.datetime.now() - waiting_period).strftime('%m-%d-%Y %H:%M:%S'))
		if dt.datetime.strptime(post[2], '%m-%d-%Y %H:%M:%S') < (dt.datetime.now() - waiting_period) and int(post[3])==0:
			results.append(post)
	return results


def get_resolved_posts(user_id):
	return query(conn, "SELECT * FROM User_Posts WHERE resolved=1 AND userid=?", (user_id, ))

def delete_post(post_id):
	query(conn, "DELETE FROM User_Posts WHERE postid=?", (post_id,))
	return


def resolve_post(post_id):
	query(conn, "UPDATE User_Posts SET resolved=1 WHERE postid=?", (post_id,))
	return


def get_post(post_id):
	return query(conn, "SELECT userid, post, timestamp, resolved FROM User_Posts WHERE postid=?", (post_id, ))
	

def get_post_content(post_id):
	return get_post(post_id)[0][1];


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

def userid_to_name(user_id):
	return ""


def username_to_id(username, name):
	return 1

def get_email(user_id):
	return ""



