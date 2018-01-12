import tweepy
import random

from time import sleep
from tb_wannabe_info import work_list

tweet_template = "L'{} de demain sera informaticien·ne !"

def loop(api, sleep_time):
    while True:
        try:
            tweet_text = tweet_template.format(random.choice(work_list))
            print(tweet_text)
            api.update_status(tweet_text)
            sleep(sleep_time)
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)

    
