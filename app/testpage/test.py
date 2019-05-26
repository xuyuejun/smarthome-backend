# coding:utf8
from . import testpage
from flask import request, jsonify, Response
import json


@testpage.route("/", methods=['GET'])
def hello():
    temperature_value = 25
    humidity_value = 60
    return jsonify(status="success", temperature=temperature_value, humidity=humidity_value)
    # return jsonify({'name': name, 'words': words})  # 也可以传入key=value形式的参数，如jsonify(name=name,words=words)


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
