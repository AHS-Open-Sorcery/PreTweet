from data_retrieval import *
import emailer
from login.config import Config
from sentiment_analysis import *
import tweepy


def send_email(user_id, post_id): # Note: can determine user_id from post_id
	emailer.send_email(Config.EMAIL_SENDER, get_email(user_id), get_post_content(post_id), Config.EMAIL_PASSWORD)
	return


def notify_users():
	users = get_all_users()
	
	for user in users:
		posts = get_expired_posts(user[0])
		for post in posts:
			send_email(user[0], post[0])


def postTweet(tweet):
    query(access_accounts(), "SELECT token FROM flask_dance_oauth WHERE id=?;", (current_user.get_id(), ))
    x = json.loads(cursor.fetchone()[0])
    auth = tweepy.OAuthHandler(Config.TWITTER_OAUTH_CLIENT_KEY, Config.TWITTER_OAUTH_CLIENT_SECRET)
    auth.set_access_token(x["oauth_token"], x["oauth_token_secret"])
    api = tweepy.API(auth)
    api.update_status(tweet)
    return


#send_email(1, 3)

