from data_retrieval import *
import emailer
from login.config import Config
from sentiment_analysis import *


def send_email(user_id, post_id): # Note: can determine user_id from post_id
	emailer.send_email(Config.EMAIL_SENDER, get_email(user_id), get_post_content(post_id), Config.EMAIL_PASSWORD)
	return

def notify_users():
	users = get_all_users()
	
	for user in users:
		posts = get_expired_posts(user[0])
		for post in posts:
			send_email(user[0], post[0])

#send_email(1, 3)
