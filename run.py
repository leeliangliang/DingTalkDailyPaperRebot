from app import app
import dingdingDailyRebot

if __name__ == '__main__':
    # 启动钉钉提醒
    dingdingDailyRebot.runTask()
    app.run(host='0.0.0.0', port=5000)

