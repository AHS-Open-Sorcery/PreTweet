import dataRetrieval
import emailer
import secrets



def send_email(user_id, post_id): # Note: can determine user_id from post_id
	emailer.send_email(secrets.sender, dataRetrieval.get_email(user_id), get_post_content(post_id), secrets.sender_password)
	return



