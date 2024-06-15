from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/index')
def index():
    uname = request.args.get('uname')
    # 判断用户名密码是否正确
    return f'欢迎登录{uname}'


app.run(debug=True)
