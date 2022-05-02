import tweepy as twitter
import secrets
import datetime
import time

auth = twitter.OAuthHandler(secrets.API_KEY, secrets.API_SECRET_KEY)
auth.set_access_token(secrets.ACCESS_TOKEN, secrets.SECRET_ACCESS_TOKEN)
api = twitter.API(auth)

def bot(hashtags):
    while True:
        print(datetime.datetime.now())

        for hashtag in hashtags:
            for tweet in twitter.Cursor(api.search_tweets, q=hashtag, count=1).items(5):
                try:
                   id=dict(tweet._json)['id']
                   text =dict(tweet._json)['text']
                   api.retweet(id) #favorites
                   api.create_favorite(id) #loves/likes
                   print("Tweet ID:", id)
                   print("Tweet Text:", text)
                except twitter.errors.TweepyException as e:
                    print(e)
        time.sleep(10)

bot(['covidlifenepali'])












