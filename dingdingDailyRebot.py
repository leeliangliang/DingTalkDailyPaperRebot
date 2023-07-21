import datetime
import pytz

from dingtalkchatbot.chatbot import DingtalkChatbot
from chinese_calendar import is_workday
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
import os
# 获取环境变量中的参数
parameter = os.environ.get('access_token')
secret = os.environ.get('secret')
# 钉钉机器人的Webhook地址
webhook = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % parameter
# 创建钉钉机器人实例
bot = DingtalkChatbot(webhook, secret)


# 定义发送消息的函数
def send_dingtalk_message(message):
    bot.send_text(msg=message, is_at_all=True)


# 判断是否是节假日
def is_needSendMsg():
    now = datetime.datetime.now()
    print("本地时间:", now)
    # 创建中国标准时间的时区对象
    cst_tz = pytz.timezone('Asia/Shanghai')
    # 将当前时间转换为中国标准时间
    now_cst = now.astimezone(cst_tz)
    print("上海时间:", now_cst.time())
    # 获取转换后的日期
    today_cst = now_cst.date()
    return is_workday(today_cst)


# 定时发送消息函数
def schedule_send_message():
    if is_needSendMsg():
        message = '@所有人 请发送今日日报。'
        send_dingtalk_message(message)
    else:
        print("节假日不发送:")

def openSpscheduler():
    # 创建调度器
    scheduler = BackgroundScheduler(timezone='Asia/Shanghai')
    # 添加定时任务
    scheduler.add_job(schedule_send_message, 'cron', misfire_grace_time=120, hour=17, minute=30)
    # scheduler.add_job(schedule_send_message, 'interval', seconds=5)
    # 启动调度器
    scheduler.start()


def runTask():
    # 判断参数是否存在
    if parameter:
        print("传入的参数:", parameter)
        if secret:
            print("传入的参数:", secret)
            openSpscheduler()
        else:
            print("未传入secret参数")
    else:
        print("未传入parameter参数")

if __name__ == '__main__':
    runTask()