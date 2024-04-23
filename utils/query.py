from pymysql import *  # 数据库驱动

conn = connect(host='localhost', port=3306, user='root', password='123456', database='weiboarticles')
cursor = conn.cursor()


def query(sql, params, type="no select"):
    params = tuple(params)
    cursor.execute(sql, params)
    conn.ping(reconnect=True)  # 连续多次query会报错，写这个可以阻拦每一次请求

    if type != 'no select':
        data_list = cursor.fetchall()  # 查询所有数据
        conn.commit()  # 提交
        return data_list
    else:
        conn.commit()