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
        return f'[id:{self.id} |  url: {self.url}]'

@app.route('/clash')
def clash():
    # 数据对象
    tasks = ClashSubscribe.query.all()
    urls = []
    for model in tasks:
        urls.append(model.url)

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

@app.route('/clashindex')
def clashindex():
    tasks = ClashSubscribe.query.all()
    return render_template('clash.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    new_task = ClashSubscribe(url=task)
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for('clashindex'))

@app.route('/delete/<int:index>')
def delete(index):
    task = ClashSubscribe.query.filter_by(id=index).first()
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('clashindex'))

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
    task = ClashSubscribe.query.filter_by(id=index).first()
    if task:
        task.url = request.form.get('new_task')
        db.session.commit()
    return redirect(url_for('clashindex'))

if __name__ == '__main__':
    app.run(debug=True)
