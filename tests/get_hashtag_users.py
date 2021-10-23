import argparse
import os
import sys
from config import * 

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")
parser.add_argument("hashtags", type=str, nargs="+", help="hashtags")
args = parser.parse_args()

bot = Bot()
bot.login(username=USERNAME, password=PASSWORD) # , proxy='127.0.0.1:8118')

#concorrente = ''
for hashtag in args.hashtags:
    users = bot.get_hashtag_users(hashtag)
    print(users)
    print(hashtag)