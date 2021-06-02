import requests
import time

token = '1830651233:AAH64rmPGjcgMGDblRYkc4AMadENLaA1o0w'

######welcome message function#####

def welcome_msg(item):
    chat_id = item["message"]["chat"]["id"]
    user_id = item["message"]["new_chat_member"]["id"]
    user_name = item["message"]["new_chat_member"].get("username",user_id)

    welcome_msg = '''
                <a href="tg://user?id={}">@{}</a> , Welcome to this group. Please read rules of the group and adhere to
                '''.format(user_id,user_name)
    to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token,chat_id,welcome_resp = requests.get(to_url))

##########################################

import datetime

endTime = datetime.datetime.now() + datetime.timedelta(minutes=3)

old_id = 202990996

while endTime > datetime.datetime.now():
    time.sleep(1)
    base_url = 'https://api.telegram.org/bot{}/getUpdates'.format(token)
    resp = requests.get(base_url)
    data = resp.json()
    for item in data["result"]:
        new_id = item["update_id"]
        if old_id < new_id:
            old_id = int(item["update_id"])
            print(item)
            try:
                if "new_chat_member" in item["message"]:
                    welcome_msg(item)
            except:
                pass
