import tweepy
import random

from time import sleep
from tb_wannabe_info import work_list

from numpy.random import choice

tweet_template = " de demain sera {}, {} !"

begins = {
    'a': ('l\'', 'l\''),
    'e': ('l\'', 'l\''),
    'é': ('l\'', 'l\''),
    'h': ('l\'', 'l\''),
    'i': ('l\'', 'l\''),
    'o': ('l\'', 'l\''),
    'u': ('l\'', 'l\'')
}

ends = ('informaticien', 'informaticienne')

order = [(1, 0), (0, 1)]

hastags = ["#infomatique", "#digital", "#numerique", "#travail", "#changement",
           "#bot"]

def loop(api, sleep_time):
    random.shuffle(work_list)
    i = 0
    while True:
        if i == len(work_list):
            i = 0
            random.shuffle(work_list)
        
        work = random.choice(work_list)
        begin = begins.get(work[0][0], ('le', 'la'))
        v = choice(len(order), 1, p=[0.6, 0.4])
        who_first = order[choice(len(order), 1, p=[0.6, 0.4])[0]]
        
        if begin[0] == 'l\'':
            if work[0] == work[1]:
                work_str = '{} {}'.format(begin[0], work[0])
            else:
                work_str = "{}{}, {}{}".format(begin[who_first[0]],
                                               work[who_first[0]],
                                               begin[who_first[1]],
                                               work[who_first[1]])
        else:
            work_str = "{} {}, {} {}".format(begin[who_first[0]],
                                             work[who_first[0]],
                                             begin[who_first[1]],
                                             work[who_first[1]])

        work_str = 'L' + work_str[1:]

        tweet_text = work_str + tweet_template.format(ends[who_first[0]],
                                                      ends[who_first[1]])
        tweet_text += " " + random.choice(hastags)

        print(tweet_text)
        try:
            api.update_status(tweet_text)
            sleep(sleep_time)
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)
        i += 1
    
