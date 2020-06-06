from dataRetrieval import *
from emailer import *
from login.config import Config
from sentiment_analysis import *


def send_email(user_id, post_id): # Note: can determine user_id from post_id
	emailer.send_email(Config.EMAIL_SENDER, dataRetrieval.get_email(user_id), dataRetrieval.get_post_content(post_id), Config.EMAIL_PASSWORD)
	return



#send_email(1, 3)
