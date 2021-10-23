from instabot import Bot
from config import * 
import requests
    
def main():    
    url='https://www.instagram.com/accounts/login/'
    import requests
    
    r = requests.Session().get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_7_3 rv:3.0; sl-SI) AppleWebKit/533.38.2 (KHTML, like Gecko) Version/5.0 Safari/533.38.2'})

    #url = 'https://www.instagram.com/accounts/login/'
    url_main = url + 'ajax/'
    req1 = requests.get(url)
    print(r.text) 

    auth = {'username': username, 'password': password}
    
    headers = {
        'origin': "https://www.instagram.com",
        'x-instagram-ajax': "1",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "*/*",
        'x-requested-with': "XMLHttpRequest",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36",
        'x-csrftoken': req1.cookies['csrftoken'],
        'referer': "https://www.instagram.com/accounts/login/",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        'cookie': "fbm_124024574287414=base_domain=.instagram.com; ig_or=landscape-primary; ig_pr=1; ig_vw=1920; mid=Wcp3vAALAAGjSka8GEnPwijnia6-; rur=FTW; ig_vh=949; csrftoken="+req1.cookies['csrftoken']+"; fbsr_124024574287414=jSVsTpoGuOgZQB0vEP_X70hrO2-LlfD9EnUz9nwGTXo.eyJhbGdvcml0aG0iOiJITUFDLVNIQTI1NiIsImNvZGUiOiJBUUMyM1FOT2ZwQU1oRVVudldzeGp1dHpwckEyODBLbUZseVo4VjVMMVVRVkJYbUVadHFyd25nekdtdzg2ejFTajRIYzVSWVRISHlvTjZXU29ScEdDZXB5RnRTMDloRXlLT3dXbU5uTTloQV9PTFE2VUI2ZFhPWW5Qa3pBNlNSZkFpSWZiU2N2anEyRFZna2FMdkdDWkRBQklCbElhYVAya2JNZzJBQW9fU0lzS3Z5NDhHRXB2RjFwQmdKOHNrdjltZWtYbFF1Z1dib040UXlzM2lwUTVfRUsxTjJUaHBpb3g1QUF2SDNpSVE2Qm1fdTFSeTZTVHFZMWR1M2NCSU5FRHpiZXRaRjFvSXY1MGJzLWFWQk4tcmFsVHY1dGE2VS13ajZCUXE0UlFEQjVHZEdqeDZpZkdlc0JsYnZvQUNlVFFJQ3pVSl9id1F1eGpyc0UxbEFzalRWZCIsImlzc3VlZF9hdCI6MTUxODg4NDA1MCwidXNlcl9pZCI6IjEwMDAyMzcyMDI5NTQyNyJ9",
        'x-compress': "null",
        'cache-control': "no-cache"
    }
    req2 = requests.post(url_main,data=auth,headers=headers)
    sessionid = req2.cookies['sessionid']

    print(req2.content)
    print(req2.cookies['ds_user_id'])
    print(req2.cookies['sessionid'])

    #Username='username'
    #Password='password'

    #requests.Session().get(url)
    #csrftoken = requests.Session().cookies['csrftoken']
    #Setting some headers and refers
    
    session = requests.Session()
    session.headers = {'user-agent': USER_AGENT}
    session.headers.update({'Referer': BASE_URL})


    try:
        #Requesting the base url. Grabbing and inserting the csrftoken

        req = session.get(BASE_URL)
        session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})
        login_data = {'username': username, 'password': password}

        #Finally login in
        login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)
        session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
        cookies = login.cookies

        #Print the html results after I've logged in
        print(login.text)

    # # with requests.Session() as session:
    # #     session.get(url)
    # #     csrftoken = session.cookies['csrftoken']
    # #     login_data = dict(csrfmiddlewaretoken=csrftoken, username=username, password=password, next=url )
    # #     session.post(url, data=login_data, headers={'Referer' : "https://python-forum.io"})
    # #     page = session.get('https://python-forum.io/usercp.php')

    #In case of refused connection
    except requests.exceptions.ConnectionError:
        print("Connection refused")
    
    
        bot = Bot( proxy = proxies['https'], 
                max_likes_per_day = 10)
        
        bot.login(username=username,
              password=password,
              proxy=proxies['https'])
        
                # max_likes_per_day=100,
                # max_unlikes_per_day=100,
                # max_follows_per_day=35,
                # max_unfollows_per_day=10,
                # max_comments_per_day=10,
                # max_likes_to_like=25,
                # filter_users=True,
                # max_followers_to_follow=250,
                # min_followers_to_follow=10,
                # max_following_to_follow=50,
                # min_following_to_follow=1,
                # max_followers_to_following_ratio=10,
                # max_following_to_followers_ratio=2,
                # max_following_to_block=200,
                # min_media_count_to_follow=3,
                # like_delay=10,
                # unlike_delay=10,
                # follow_delay=30,
                # unfollow_delay=30,
                # comment_delay=60,
                # stop_words=['store', 'free'])


    #bot.unfollow_non_followers()

if __name__ == "__main__":
    main()