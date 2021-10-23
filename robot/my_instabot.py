import argparse
import os
import sys
from params import * 

sys.path.append(os.path.join(sys.path[0], "../"))
from instabot import Bot  # noqa: E402

parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
parser.add_argument("-proxy", type=str, help="proxy")
parser.add_argument("users", type=str, nargs="+", help="users")
args = parser.parse_args()

bot = Bot(max_follows_per_day=3,
    filter_users=True,
    filter_private_users=False,
    filter_previously_followed=True,
    filter_business_accounts=True,
    filter_verified_accounts=True,
)

bot.login(username=USERNAME, password=PASSWORD)

for username in args.users:
    #bot.follow_followers(username)
    print(username)
