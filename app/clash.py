from urllib import parse
import requests
from app.context import flaskApp as app
from flask import Response, render_template, request, redirect, url_for
from app.db.sqlite import sqliteDB as db

# 用户模型
class ClashSubscribe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<ClashSubscribe {self.url}>'

@app.route('/clash')
def clash():
    # 数据对象
    urls = request.args.getlist('urls')
    data = {
        "url": '|'.join(urls),
        "insert": "false",
        "emoji": "true",
        "config": "http://webserver:5000/static/clashconfig/ACL4SSR_Online.ini",
        "new_name": "true",
        "tfo": "false",
        "scv": "false",
        "fdn": "false",
        "sort": "false",
        "list": "false"
    }
    # 进行url_encode编码，编码结果为查询字符串形式，即进行url编码，然后用a=1&b=2形式拼接键值对
    text = parse.urlencode(data)
    response = requests.get('http://subconverter:25500/clash?' + text)
    return Response(response.text, status=response.status_code, content_type=response.headers['content-type'])

@app.route('/')
def index():

    return render_template('clash.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if index < len(tasks):
        tasks.pop(index)
    return redirect(url_for('index'))

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
    if index < len(tasks):
        new_task = request.form.get('new_task')
        tasks[index] = new_task
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
