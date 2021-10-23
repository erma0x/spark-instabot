import argparse
import os
import sys
from params import * 

if __name__ == "__main__" :
    sys.path.append(os.path.join(sys.path[0], "../"))
    from instabot import Bot  # noqa: E402

    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-u", type=str, help="username")
    parser.add_argument("-p", type=str, help="password")
    parser.add_argument("-proxy", type=str, help="proxy")
    parser.add_argument("users", type=str, nargs="+", help="users")
    args = parser.parse_args()

    bot = Bot(max_follows_per_day=3)

    bot.login(username=USERNAME, password=PASSWORD)

    for username in args.users:
        bot.follow_followers(username)
        #print(username)
