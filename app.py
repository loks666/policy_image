import re

from flask import Flask, session, request, render_template
from flask import jsonify
from werkzeug.utils import redirect

from utils.bertopic.bertopic_util import save_data2db
from views.page import page
from views.user import user

app = Flask(__name__)
app.secret_key = 'secrect_key'
app.register_blueprint(page.pb)  # 注册
app.register_blueprint(user.ub)  # 注册


@app.route("/")
def hello_world():
    return render_template('index.html')
    return session.clear()


@app.route("/save_data", methods=['GET', 'POST'])
def save_data():
    try:
        # 调用save_data2db函数
        save_data2db()
        # 如果函数执行成功，返回HTTP状态码200和成功消息
        return jsonify({'code': 200, 'message': '保存数据成功!'})
    except Exception as e:
        # 如果函数执行失败，返回HTTP状态码500和失败消息
        return jsonify({'code': 500, 'message': '保存数据失败!', 'error': str(e)}), 500

@app.route("/save_data", methods=['GET', 'POST'])
def save_data():
    try:
        # 调用save_data2db函数
        save_data2db()
        # 如果函数执行成功，返回HTTP状态码200和成功消息
        return jsonify({'code': 200, 'message': '保存数据成功!'})
    except Exception as e:
        # 如果函数执行失败，返回HTTP状态码500和失败消息
        return jsonify({'code': 500, 'message': '保存数据失败!', 'error': str(e)}), 500


@app.route("/generate_model", methods=['GET', 'POST'])
def generate_model():
    try:
        generate_model()
        return jsonify({'code': 200, 'message': '生成模型成功!'})
    except Exception as e:
        # 如果函数执行失败，返回HTTP状态码500和失败消息
        return jsonify({'code': 500, 'message': '生成模型失败!', 'error': str(e)}), 500


@app.route("/load_model")
def load_model():
    return render_template('index.html')
    return session.clear()


@app.before_request
def before_request():
    pat = re.compile(r'^/static')  # 访问静态目录,非法输入会拦截， 比如/user/123会跳转到/user/login
    # print(session.get('username'))
    if re.search(pat, request.path):
        return
    elif request.path == '/user/login' or request.path == '/user/register':
        return
    elif session.get('username'):
        return
    return redirect('/user/login')


@app.route('/<path:path>')
def catch_all(path):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
