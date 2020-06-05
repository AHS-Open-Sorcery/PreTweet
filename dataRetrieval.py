import sqlite3
from sqlite3 import Error
from datetime import *
import time


def establish_connection(file):
	try: 
		connection = sqlite3.connect(file)
		return connection
	except Error as e:
		print(e)
	
	return None


def query(connection, command):
	cursor = connection.cursor()
	cursor.execute(command)
	results = cursor.fetchall()
	cursor.close()
	return results


conn = establish_connection("persistence.db")
waiting_period = timedelta(seconds=1)




def get_user_posts(user_id):
	posts = query(conn, "SELECT post, timestamp FROM User_Posts WHERE userid='{}'".format(user_id))
	return posts;

def add_user_post(user_id, post, timestamp=datetime.now()):
	query(conn, "INSERT INTO User_Posts (userid, post, timestamp) VALUES ('{}', '{}', '{}')".format(user_id, post, timestamp))
	return

def get_expired_posts():
	posts = query(conn, "SELECT userid, post FROM User_Posts WHERE timestamp<'{}'".format(datetime.now() - waiting_period))
	return posts;


"""
#Testing Code:

add_user_post(1, "hi")
add_user_post(2, "hi~")
add_user_post(2, "bye")
add_user_post(1, "Bye")

print(get_user_posts(1))
print(get_user_posts(2))

time.sleep(2)

add_user_post(1, "hey")
add_user_post(2, "hay")

print(get_user_posts(1))
print(get_user_posts(2))
print(get_expired_posts())
"""

