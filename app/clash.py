from urllib import parse
import requests
from app.context import flaskApp as app
from flask import request, Response


@app.route('/clash')
def clash():
    # 数据对象
    urls = request.args.getlist('urls')
    data = {
        "url": '|'.join(urls),
        "insert": "false",
        "emoji": "true",
        "config": "http://192.168.2.1:5000/static/clashconfig/ACL4SSR_Online.ini",
        "new_name": "true",
        "tfo": "false",
        "scv": "false",
        "fdn": "false",
        "sort": "false",
        "list": "false"
    }
    # 进行url_encode编码，编码结果为查询字符串形式，即进行url编码，然后用a=1&b=2形式拼接键值对
    text = parse.urlencode(data)
    response = requests.get('http://192.168.2.1:25500/clash?' + text)
    return Response(response.text, status=response.status_code, content_type=response.headers['content-type'])