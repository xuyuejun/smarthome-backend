from . import humidity
from flask import request
import random
import time
import jsonify


@humidity.route("/getLatest", methods=['GET', 'OPTIONS'])
def login():
    if request.method == "GET":
        humi = random.randint(1, 100)  # 湿度模拟
        recordtime = int(time.time())
        s = ['张三', '年龄', '姓名']
        return jsonify(s)
    elif request.method == "OPTIONS":
        print('OPTIONS方法')
        return "fuck you"
    else:
        return "<h1>login Failure !</h1>"
