'''
Created on 2018年1月4日

@author: 孤
'''
import requests
import itchat
from itchat.content import INCOME_MSG, NOTE, TEXT, MAP, CARD, SHARING, PICTURE,\
    RECORDING, ATTACHMENT, VIDEO
from itchat.components import hotreload

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


#-------------------------------------------------------
#对特定的消息自动回复
# @itchat.msg_register(INCOME_MSG)
# def text_reply(msg):    #监听文字消息
#     print(msg)
#     if not msg["FromUserName"]==myUserName:
#         if msg["Text"]=="你好":
#             return "你好,我是张耀烽"
#         return "撒拉嘿呦,过会联系哦"
#     else:
#         return "自己给自己发消息没意思"
#-------------------------------------------------------

#回复普通聊天
@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def single_reply(msg):
    print(msg)
    if msg['Type'] == TEXT:
        defaultReply = 'Hello :' + msg['Text']
        if msg['Text'] in ["张耀烽","张耀峰"]:
            reply = "张耀烽是最帅的人"
        elif msg['Text'] in ["自定义Text"]:
            reply = "自定义回复"
        elif msg['Text'] in ["自定义Text"]:
            reply = "自定义回复"
        elif msg['Text'] in ["自定义Text"]:
            reply = "自定义回复"
        elif msg['Text'] in ["自定义Text"]:
            reply = "自定义回复"
        else:
            reply = get_reply(msg['Text'])
        return reply or defaultReply
    return

#回复群聊
@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING],isGroupChat=True)
def group_reply(msg):
    defaultReply = 'Hello:' + msg['Text']   #如果图灵机器失效时回复消息
    reply = ""
    if msg['Type'] == TEXT:
        if "张耀烽" in msg['Text']:
            reply = "帅就一个字"
        elif "自定义Text" in msg['Text']:
            reply = "帅就一个字"
        elif "自定义Text" in msg['Text']:
            reply = "帅就一个字"
        else:
            if msg['isAt']:
                rel_msg = msg['Text'].split("@秋枫丶\u2005")
                if rel_msg[1]:
                    reply = get_reply(rel_msg[1])
                else:
                    reply = "@我干什么"
                ret = reply or defaultReply
                return ret

#处理图片,语音,附件,小视频
@itchat.msg_register([PICTURE,RECORDING,ATTACHMENT,VIDEO],isGroupChat=True)
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE:'img',
        VIDEO:'vid'}.get(msg.type,'fil')
    return '@%s@%s' % (typeSymbol,msg.filename)


#监听事件
if __name__ == "__main__":
    try:
        itchat.auto_login()#hotReload=True
        myUserName = itchat.get_friends(update=True)[0]["UserName"]
        itchat.run()    #监控信息
    except:
        print("has except")