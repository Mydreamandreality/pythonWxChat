'''
Created on 2018年1月4日

@author: 孤
'''
import requests
import itchat
from itchat.content import *

#调用图灵机器人接口
KEY = "39278b6004c64cb5b39bb5334c391450"
UID = 'my'

def get_reply(msg):
    api_tuling = 'http://www.tuling123.com/openapi/api'
    data = {
        'key':KEY,
        'info':msg,
        'userid':UID,
    }
    try:
        ret = requests.post(api_tuling, data=data).json()
        return ret.get("text")
    except:
        return
    
    
msgger = get_reply('北京天气')
print(msgger)
    