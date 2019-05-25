from . import servocontrol


@servocontrol.route("/")
def index():
    return "<h1 style='color:red'>云台控制<h1>"
