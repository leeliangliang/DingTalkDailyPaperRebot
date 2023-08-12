from flask import render_template, redirect, url_for, session, g
from flask import request
from app.context import flaskApp as app
from app.db.sqlite import sqliteDB as db

# 用户模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

# 登录页面
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # 验证用户输入的用户名和密码
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            # 登录成功，设置会话并重定向到后台页面
            session['username'] = username
            return redirect(url_for('clashindex'))
        else:
            # 登录失败，显示错误信息
            error_message = 'Invalid username or password'
            return render_template('login.html', error_message=error_message)

    # GET 请求时渲染登录页面
    return render_template('login.html')

# 后台页面
@app.route('/admin')
def admin():
    # 检查用户是否已登录，若未登录则重定向到登录页面
    if 'username' not in session:
        return redirect(url_for('login'))

    # 用户已登录，渲染后台页面
    return f'Welcome to the admin page, {session["username"]}!'

# 注销
@app.route('/logout')
def logout():
    # 清除会话，实现用户注销
    session.pop('username', None)
    return redirect(url_for('login'))

