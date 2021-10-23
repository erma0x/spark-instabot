from instagrapi import Client

ACCOUNT_USERNAME = 'pratinostock'
ACCOUNT_PASSWORD = 'Ermanobuik00'

cl = Client()
cl.login(ACCOUNT_USERNAME, ACCOUNT_PASSWORD)

user_id = cl.user_id_from_username("adw0rd")
medias = cl.user_medias(user_id, 20)
