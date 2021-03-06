from flask import jsonify
from . import temperature
import Adafruit_DHT
import time


@temperature.route("/getLatest")
def getData():
    sensor = Adafruit_DHT.DHT11
    pin = 24
    humidity_value, temperature_value = Adafruit_DHT.read_retry(sensor, pin)
    getTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if humidity_value is not None and temperature_value is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature_value, humidity_value))
        return jsonify(status="Success", temperature="{:0.1f}".format(temperature_value), humidity="{:0.1f}".format(humidity_value), time=getTime)
    else:
        print('Failed to get reading. Try again!')
        return jsonify(status="failed", temperature=0, humidity=0, time=getTime)
