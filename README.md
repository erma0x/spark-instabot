# Spark Instagram Bot
Personal instagram bot for automating social media manager stuff and automatic follow up.

## 3rd party library
- https://instagrambot.github.io/docs/it/
- https://instagrambot.github.io/docs/it/How_to_use.html
- https://gist.github.com/DusanMadar/8d11026b7ce0bce6a67f7dd87b999f6b

## Installation

1. Create Virtual enviroment
``` bash 
python3 -m venv venv
```

2. Activate the enviroment          
``` bash
source venv/bin/activate
```

3. Installation for Mac and Linux
``` bash
pip3 install instabot-py
```
3. Installation for Windows

``` bash
pip install instabot-py
```
4. Install the requirements 
``` bash
pip3 install -r requirements.txt
```

5. Update library
``` bash 
pip install -U instabot 

``` 

6. If you don't have it you have to download tor and privoxy. (Debian)
``` bash 
sudo upgrade & update | sudo apt install tor | sudo apt install privoxy 

``` 

7. Activate insta avoiders
``` bash 
sudo surfshark-vpn
service privoxy start

```
8. Create .env file inside /robot/ with the following informations: <br>
Username = "MY_USERNAME" <br>
Password = "MY_PASSSWORD" <br>

8. Run the Robot in a server
``` bash 
venv/bin/python3 robot/spark-instabot.py myCompetitorUsername

```
9. Activate insta avoiders
``` bash 
sudo surfshark-vpn
service privoxy start

```

## What the bot can do
- Login to your Instagram account
- View Followers and Account you are following
- Like Photo or Video
- Follow/Unfollow Account
- Make or See Comments
- And much more ... 

![Alt text](docs/img/bot_parameters.png?raw=true)
![Alt text](docs/img/follow_methods.png?raw=true)
![Alt text](docs/img/get_methods.png?raw=true )
![Alt text](docs/img/unfollow_methods.png?raw=true )
![Alt text](docs/img/unlike_methods.png?raw=true )
![Alt text](docs/img/comments.png?raw=true)

