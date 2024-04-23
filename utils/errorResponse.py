from flask import render_template

def errorResponse(errorMsg):#封装报错函数
    return render_template('error.html', errorMsg=errorMsg)