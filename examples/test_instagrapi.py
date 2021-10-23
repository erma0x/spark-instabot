from instagrapi import Client

ACCOUNT_USERNAME = ''
ACCOUNT_PASSWORD = ''

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

user_id = cl.user_id_from_username("elon.musk")
medias = cl.user_medias(user_id, 20)
