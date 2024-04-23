from flask import Flask, session, render_template, redirect, Blueprint, request
from utils.query import query
from utils.errorResponse import errorResponse
import time

ub = Blueprint('user', __name__, url_prefix='/user', template_folder='templates')

@ub.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        def filter_fn(user):
            return request.form['username'] in user and request.form['password'] in user

        users = query('select * from user', [], 'select')
        login_success = list(filter(filter_fn, users))
        if not len(login_success): errorResponse('账号或密码错误')

        session['username'] = request.form['username']
        return redirect('/page/home')



@ub.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        if request.form['password'] != request.form['checkPassword']: return errorResponse('请保证两次密码一致')

        def filter_fn(user): #过滤重复用户名
            return request.form['username'] in user
        users = query('select * from user', [], 'select') #select参数表示查询
        # print(users)

        filter_list = list(filter(filter_fn, users))
        if len(filter_list):
            return errorResponse('该用户名已被注册')
        else:
            time_tuple = time.localtime(time.time()) #注册用户名的时间对象
            # print(time_tuple)
            query('''
                insert into user(username, password, createTime) value(%s, %s, %s)
                '''
                , [request.form['username'], request.form['password'], str(time_tuple[0]) + '-' + str(time_tuple[1]) + '-' + str(time_tuple[2])]
                ) #年-月-日


        return redirect('/user/login') #重定向到登陆页面

@ub.route('/logOut')
def logOut():
    session.clear()
    return redirect('/user/login')


