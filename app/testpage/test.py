# coding:utf8
from . import testpage
from flask import request
import json


@testpage.route("/")
def index():
    return "<h1 style='color:red'>测试页面<h1>"


@testpage.route("/login", methods=['GET', 'POST', 'OPTIONS'])
def login():
    if request.method == "POST":
        data = request.get_json()
        print(data)
        username = data['username']
        password = data['password']
        print("数据测试")
        print(username)
        print(password)
        s = [username, password]
        if username == "zhangsan" and password == "123":
            return "<h1>welcome, %s !</h1>" % username
        else:
            print("执行else")
            return json.dumps(s, ensure_ascii=False)
    elif request.method == "OPTIONS":
        print('OPTIONS方法')
        return "fuck you"
    else:
        return "<h1>login Failure !</h1>"
