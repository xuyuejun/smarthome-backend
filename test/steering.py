import sys
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# 使用14BCM

def setServoAngle(servo, angle):
    pwm = GPIO.PWM(servo, 50)
    pwm.start(8)
    dutyCycle = angle / 18. + 3.
    pwm.ChangeDutyCycle(dutyCycle)
    sleep(0.3)
    pwm.stop()


if __name__ == '__main__':
    servo = 14  # 设置服务引脚
    GPIO.setup(servo, GPIO.OUT) # 引脚为输出
    setServoAngle(servo, int(sys.argv[1]))  # 转动角度
    GPIO.cleanup()
