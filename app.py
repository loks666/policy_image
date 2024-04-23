import re
from flask import Flask, session, request, render_template
from werkzeug.utils import redirect

app = Flask(__name__)
app.secret_key = 'secrect_key' #任意值

from views.page import page
from views.user import user
app.register_blueprint(page.pb) # 注册
app.register_blueprint(user.ub) # 注册

@app.route("/")
def hello_world():
    # return render_template('index.html')
    return session.clear()

@app.before_request
def before_request():
    pat = re.compile(r'^/static') #访问静态目录,非法输入会拦截， 比如/user/123会跳转到/user/login
    # print(session.get('username'))
    if re.search(pat, request.path): return
    elif request.path == '/user/login' or request.path == '/user/register': return
    elif session.get('username'): return
    return redirect('/user/login')

@app.route('/<path:path>')
def catch_all(path):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)