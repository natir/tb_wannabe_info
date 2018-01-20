import tweepy

from . import cr
from . import tweet

def main():
    auth = tweepy.OAuthHandler(cr.consumer_key, cr.consumer_secret)
    auth.set_access_token(cr.access_token, cr.access_token_secret)
    api = tweepy.API(auth)

    tweet.loop(api, 3600/2)

if __name__ == '__main__':
    main()
