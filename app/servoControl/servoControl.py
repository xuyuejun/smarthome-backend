from . import servoControl


@servoControl.route("/")
def index():
    return "<h1 style='color:red'>云台控制<h1>"
