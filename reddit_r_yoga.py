import os
from dotenv import load_dotenv
from pathlib import Path 
import logging
import requests
import requests.auth
import json

"""Set environment variables"""
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
#Environemnt variables that contains the user credentials to access Spotify API 
"""input user name"""
username = os.getenv("user_name")
cid = os.getenv("client_id")
secret = os.getenv("client_secret")
redirect = os.getenv("redirect_uri")
app_name = os.getenv("app_name")
token = os.getenv("access_token")

print(token)

"""Authenticate"""
client_auth = requests.auth.HTTPBasicAuth(cid, secret)
post_data = {"grant_type": "password", "username": username, "password": app_name}
headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
r = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)

#headers = {"Authorization": "bearer"+token, "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
#response = requests.get("https://www.reddit.com/api/live/happening_now", headers=headers)
#try:
#    print(response.json())
#except:
#    print("cannot print happening now")

params = {"t":"day","limit":5}
headers = {'User-agent': 'bot_0.1'}

thread = "yoga"
url = 'https://www.reddit.com/r/'+thread+'/hot/.json?sort=hot&n=25'
response = requests.get(url, headers)
if response.ok:
    print(response.json())
    with open('output.py', 'w') as file:
        file.write("null=None\nfalse=False\ntrue=True\ncontent="+str(json.dumps(response.json())))
else:
    print("cannot get response")
