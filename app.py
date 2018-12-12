from flask import Flask, render_template, request, redirect,session,url_for
app = Flask(__name__)
app.debug = True  # 避免每次更改代码后，需要重启flask
app.config['SECRET_KEY'] = '123456'  # 使用session前必须设置一下密钥
USERS = {
    1: {'name': 'sjt', 'age': 22, 'gender': '男', 'text': '喜欢打篮球'},
    2: {'name': 'lyy', 'age': 22, 'gender': '女', 'text': '喜欢看电影'}
}


@app.route('/detail/<int:nid>', methods=['GET'])  # <int:nid> 代表接受url连接穿过来的参数，int代表传过来的是数字
def detail(nid):
    user = session.get('user_info')
    if not user:
        return redirect('/login')
    info = USERS.get(nid)  # 取字典的第一个数据
    return render_template('/detail.html', info=info)

@app.route('/index', methods=['GET'])
def index():
    user = session.get('user_info')
    if not user:
        url = url_for('l1')
        return redirect(url)  # 如果跳转的网站特别长的话，就需要起个别名
    return render_template('index.html', user_dict=USERS)


@app.route('/login', methods=['GET', 'POST'], endpoint='l1')  # 跟Django的name一样，相当于起个别名
def login():
    # 首先判断get请求做什么，post请求做什么，那边的form提交的账号密码，全部放入request里面了
    if request.method == 'GET':
        return render_template('login.html')
    else:
        # request.query_string  这里面放的是url提交的数据
        user = request.form.get('user')
        pwd = request.form.get('pwd')
        if user == 'alex' and pwd == '123':
            session['user'] = user
            return redirect('http://www.luffycity.com')   # 重定向，跳转到另外一个页面
        return render_template('login.html',error='用户名或密码错误')  # 这个error随便取名，是用来返回给html页面数据拿去显示的


if __name__ == '__main__':
    app.run()
