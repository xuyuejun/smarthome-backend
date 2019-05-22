# coding:utf8
from . import temperature


@temperature.route("/")
def index():
    return "<h1 style='color:red'>温度计<h1>"

