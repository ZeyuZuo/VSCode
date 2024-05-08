# encoding utf-8
# /Library/Frameworks/Python.framework/Versions/3.9/bin/python3

# 目标，每个小时通过钉钉机器人发一个消息
from dingtalkchatbot.chatbot import DingtalkChatbot
import time
from datetime import datetime


# 通过钉钉群机器人发消息
def SayHello():
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=54803e6bdc1a0bc438ecc97c1ace78f2eb7dfe101298ab24682618429cc0c320'
    secret = 'SECbc64bc7f21cc7aba5cb444dbdedfd82b14aea021229f654c22c199a255c39cd5'  # 可选：创建机器人勾选“加签”选项时使用
    xiaoding = DingtalkChatbot(webhook, secret=secret)
    msg = '提醒喝水小助手，每隔1小时提醒一次。现在的时间是：'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    xiaoding.send_text(msg=msg)


SayHello()