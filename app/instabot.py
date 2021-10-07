from instabot import Bot
import config

strategy_description="""

-------------- STRATEGIA ----------------------------------------------------


1)  Inserire manualmente lista dei concorrenti in config.py.

2)  Il bot deve fare data scraping per mettere tutti gli utenti che seguono
    i concorrenti su un file chimato whitelist.txt. 

3)  Cancello i doppioni degli username dalla lista dei whitelist.txt 

4)  Metti follow ed un like a tutti gli utenti che seguono i concorrenti
    con una frequenza di 5 ogni ora ad intervalli casuali.


--------------- REGOLE ----------------------------------------------------
 
Ogni follower che ho gia' seguito non lo voglio riseguire, quindi 
appena faccio follow a qualcuno lo cancello da whitelist.txt e lo metto su blacklist.txt

Ogni 5 giorni smetti di seguire chi non ti segue.


Non lavorare MAI dalle 19:00 alle 9:00. O di sabato e di domenica.
----------------------------------------------------------------------------

"""


def main():
    bot = Bot(
                proxy=None,
                max_likes_per_day=1000,
                max_unlikes_per_day=1000,
                max_follows_per_day=350,
                max_unfollows_per_day=350,
                max_comments_per_day=100,
                max_likes_to_like=100,
                filter_users=True,
                max_followers_to_follow=2000,
                min_followers_to_follow=10,
                max_following_to_follow=7500,
                min_following_to_follow=10,
                max_followers_to_following_ratio=10,
                max_following_to_followers_ratio=2,
                max_following_to_block=2000,
                min_media_count_to_follow=3,
                like_delay=10,
                unlike_delay=10,
                follow_delay=30,
                unfollow_delay=30,
                comment_delay=60,
                whitelist=False,
                blacklist=False,
                comments_file=False,
                stop_words=['shop', 'store', 'free']
            )

    bot.login(username=config.username, password=config.password)

    bot.unfollow_non_followers()



if __name__ == "__main__":
    main()