from flask import Blueprint, render_template

temperature = Blueprint('temperature',__name__)

@temperature.route("/getTemp")
def getTemp():
    return "获取温度"
