from flask import Flask
import os

flaskApp = Flask(__name__, template_folder='templates')
# 设置静态文件的路径
flaskApp.static_folder = 'static'
# 设置静态文件的 URL 路径
flaskApp.static_url_path = '/static'
#
flaskApp.secret_key = os.environ.get('secret_key')
