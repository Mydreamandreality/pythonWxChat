'''
Created on 2018年1月4日

@author: 孤
'''
import itchat
from itchat.components import hotreload
#itchat登录微信
itchat.auto_login(hotReload=True)  #Hotreload=true代表默认使用登录
#发消息
itchat.send('hello 你好', toUserName="filehelper")
#给文件助手发送一张图片
itchat.send("@img@wallhaven-554748.jpg",toUserName="filehelper")

#给特定的好友发送消息
#,获取我的好友列表,第一个是自己
friends = itchat.get_friends(update=True) #update代表如果好友列表更新则重新获取
#获取第一个好友信息
friedns_fir = friends[1]
#username代表hascode值,NickName代表微信名称,RemarkName代表备注名称
print(friedns_fir['UserName'],friedns_fir["NickName"],friedns_fir["RemarkName"])
#发送消息
itchat.send("Hello-\n消息来自智能机器人 %s"%(friedns_fir["NickName"]),toUserName=friedns_fir['UserName'])

