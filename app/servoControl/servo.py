import sys
import RPi.GPIO as GPIO
from time import sleep
from . import servocontrol
from flask import request, jsonify


def setServoAngle(servo, angle):
    pwm = GPIO.PWM(servo, 50)
    pwm.start(8)
    dutyCycle = angle / 18. + 3.
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(0.3)
    pwm.stop()


@servocontrol.route('/horizontal', methods=['GET'])
def get_task():
    if not request.args or 'angle' not in request.args:
        return "无输入数据"
    else:
        servo = 14  # 设置服务引脚
        angle = request.args['angle']  # 转动角度
        print(angle)
        setServoAngle(servo, int(angle))
        GPIO.cleanup()
        return "成功控制"
