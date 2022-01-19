import argparse
import os
import sys
from params import * 

from instabot import Bot

def main():

    # try:

        sys.path.append(os.path.join(sys.path[0], "../"))
        
        parser = argparse.ArgumentParser(add_help=True)
        # parser.add_argument("-u", type=str, help="username")
        # parser.add_argument("-p", type=str, help="password")

        parser.add_argument("competitor_username", type=str, nargs="+", help="your competitor username")
        args = parser.parse_args()
        
        bot = Bot(max_follows_per_day=5,
                max_likes_per_day=2,
                max_likes_to_like = 2,
                filter_users=False,
                max_followers_to_follow=40,
                min_followers_to_follow=1,
                max_following_to_block=1
                )

        bot.login(username=Username, password=PAssword)

        print('Login - OK')
        print('username',Username, 'password',PAssword)

        for username in args.users:
            bot.follow_followers(username)

    # except:
    #     print(' Sorry, something went wrong')
        
if __name__ == "__main__" :
    main()

