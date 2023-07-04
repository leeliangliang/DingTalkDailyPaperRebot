import time
from dingtalkchatbot.chatbot import DingtalkChatbot
import holidays
from apscheduler.schedulers.blocking import BlockingScheduler
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
def is_holiday(date):
    us_holidays = holidays.CN()
    return date in us_holidays


# 定时发送消息函数
def schedule_send_message():
    current_date = time.strftime('%Y-%m-%d', time.localtime())
    if not is_holiday(current_date):
        message = '@所有人 请发送今日日报。'
        send_dingtalk_message(message)
    else:
        print("节假日不发送:")

def startTask():
    # 创建调度器
    scheduler = BlockingScheduler(timezone='Asia/Shanghai')
    # 添加定时任务
    scheduler.add_job(schedule_send_message, 'cron', hour=17, minute=30)
    # scheduler.add_job(schedule_send_message, 'interval', seconds=5)
    # 启动调度器
    scheduler.start()


if __name__ == '__main__':

    # 判断参数是否存在
    if parameter:
        print("传入的参数:", parameter)
        if secret:
            print("传入的参数:", secret)
            startTask()
        else:
            print("未传入secret参数")
    else:
        print("未传入parameter参数")
