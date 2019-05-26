from flask import request, jsonify, Response
from . import temperature
import RPi.GPIO as GPIO
import time


@temperature.route("/getLatest")
def getData():
    channel = 24  # 引脚号16
    data = []  # 温湿度值
    j = 0  # 计数器

    GPIO.setmode(GPIO.BCM)  # 以BCM编码格式
    time.sleep(1)  # 时延一秒
    GPIO.setup(channel, GPIO.OUT)
    GPIO.output(channel, GPIO.LOW)
    time.sleep(0.02)  # 给信号提示传感器开始工作
    GPIO.output(channel, GPIO.HIGH)
    GPIO.setup(channel, GPIO.IN)

    while GPIO.input(channel) == GPIO.LOW:
        continue
    while GPIO.input(channel) == GPIO.HIGH:
        continue
    while j < 40:
        k = 0
        while GPIO.input(channel) == GPIO.LOW:
            continue
        while GPIO.input(channel) == GPIO.HIGH:
            k += 1
            if k > 100:
                break
        if k < 8:
            data.append(0)
        else:
            data.append(1)
        j += 1

    print("sensor is working.")
    print(data)  # 输出初始数据高低电平

    humidity_bit = data[0:8]  # 分组
    humidity_point_bit = data[8:16]
    temperature_bit = data[16:24]
    temperature_point_bit = data[24:32]
    check_bit = data[32:40]

    humidity_value = 0
    humidity_point = 0
    temperature_value = 0
    temperature_point = 0
    check = 0

    for i in range(8):
        humidity_value += humidity_bit[i] * 2 ** (7 - i)  # 转换成十进制数据
        humidity_point += humidity_point_bit[i] * 2 ** (7 - i)
        temperature_value += temperature_bit[i] * 2 ** (7 - i)
        temperature_point += temperature_point_bit[i] * 2 ** (7 - i)
        check += check_bit[i] * 2 ** (7 - i)

    tmp = humidity_value + humidity_point + temperature_value + temperature_point  # 十进制的数据相加
    GPIO.cleanup()
    if check == tmp:  # 数据校验，相等则输出
        return jsonify(status="Success", temperature=temperature_value, humidity=humidity_value)
    else:
        return jsonify(status="failure", temperature=temperature_value, humidity=humidity_value, check=check, tmp=tmp)   # 错误输出错误信息，和校验数据
