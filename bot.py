#IMPORTS
import tweepy
import time
import random

#METHODS
def authenticate(consumer_key, consumer_secret, access_token, access_token_secret):
    print("Authenticating...")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    print("...Authenticated!")
    return tweepy.API(auth)

def search_for_user_recent_tweets(user_id):
    global searches_performed
    user_tweets = api.user_timeline(id=user_id, since_id=tweet_for_date_reference)
    user_tweets = [tweet for tweet in user_tweets if not ((tweet.text.startswith("RT @")) or (tweet.in_reply_to_status_id is not None))]
    searches_performed = searches_performed + 1
    return user_tweets

def responder_tweet(tweet):
    global replies
    try:
        api.create_favorite(tweet.id)
        api.update_status(status="@" + tweet.author.screen_name + " " + random.choice(phrases), in_reply_to_status_id=tweet.id)
        replies = replies + 1
    except:
        pass

#CONSTRAINTS
consumer_key = 'XXXXX'
consumer_secret = 'XXXXX'
access_token = "XXXXX-XXXXX"
access_token_secret = "XXXXX"
user_id = 1029916827340742657
tweet_for_date_reference = 1270422995140513794
phrases = ["puta crítica cirúrgica do gama", "essa aí foi cirúrgica dms", "gama sempre cirúrgico em seus post", "essa aí não foi cirúrgica e sim muito precisa"]
searches_performed = 0
replies = 0

#TODO CODE
api = authenticate(consumer_key, consumer_secret, access_token, access_token_secret)
print("\nBot started!\n")
while True:
    try:
        tweets_list = search_for_user_recent_tweets(user_id)
        for tweet in tweets_list:
            responder_tweet(tweet)
            tweet_for_date_reference = tweet.id
        print("===INFO===\nSearches performed: " + str(searches_performed) + "\nReplies total: " +str(replies))
        time.sleep(1.5*60)
    except tweepy.RateLimitError:
        print("===INFO===\nRate limit reached... resting for 15 minutes...")
        time.sleep(15 * 60)
