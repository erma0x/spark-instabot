from instabot import Bot
from config import * 
import requests
    
def main():    
    
    Username='username'
    Password='password'
    
    url = 'https://www.instagram.com/accounts/login/'
    
    auth = {'username': Username, 'password': Password}
    
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
 
    print('*'*80)
    print(' Start session metadata ')

    r = requests.Session().get(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_7_3 rv:3.0; sl-SI) AppleWebKit/533.38.2 (KHTML, like Gecko) Version/5.0 Safari/533.38.2'})
    url_main = url + 'ajax/'
    req1 = requests.get(url)
    print(r.text)
    
    requests.Session().get(url)
    csrftoken = requests.Session().cookies['csrftoken']
    print(csrftoken)
    session = requests.Session()
    session.headers = {'user-agent': USER_AGENT}
    session.headers.update({'Referer': BASE_URL})
    print(' End Session metadata ')
    print('*'*80)


    try:
         
        req = session.get(BASE_URL) #Requesting the base url. Grabbing and inserting the csrftoken
        session.headers.update({'X-CSRFToken': req.cookies['csrftoken']})
        login_data = {'username': username, 'password': password}

        login = session.post(LOGIN_URL, data=login_data, allow_redirects=True)
        session.headers.update({'X-CSRFToken': login.cookies['csrftoken']})
        cookies = login.cookies

        print(login.text) #Print the html results after I've logged in

        bot = Bot( proxy = proxies['https'],          # init Bot 4 Instagram
                max_likes_per_day = 10)
        
        bot.login(username=username,                
              password=password,
              proxy=proxies['https'])

        bot.unfollow_non_followers()

    #In case of refused connection
    except requests.exceptions.ConnectionError:
        print(" ==> Connection Refused")
        print(requests.exceptions.ConnectionError)

if __name__ == "__main__":
    main()