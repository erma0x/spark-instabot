import argparse
import os
import sys
from params import * 
from dotenv import load_dotenv

def main():

    # try:
        from instabot import Bot
        load_dotenv()
        USERNAME = os.getenv('Username')
        PASSWORD = os.getenv('Password')
        sys.path.append(os.path.join(sys.path[0], "../"))
        
        parser = argparse.ArgumentParser(add_help=True)
        parser.add_argument("-u", type=str, help="username")
        parser.add_argument("-p", type=str, help="password")
        parser.add_argument("-proxy", type=str, help="proxy")
        parser.add_argument("competitor_username", type=str, nargs="+", help="your competitor username")
        args = parser.parse_args()
        
        bot = Bot(max_follows_per_day=3,
                max_likes_per_day=20,
                max_likes_to_like = 150,
                filter_users=True,
                max_followers_to_follow=3000,
                min_followers_to_follow=10,
                max_following_to_block=2000
                )

        bot.login(username=USERNAME, password=PASSWORD)

        print('Login - OK')
        print('username',USERNAME, 'password',PASSWORD)

        for username in args.users:
            bot.follow_followers(username)

    # except:
    #     print(' Sorry, something went wrong')
        
if __name__ == "__main__" :
    main()

