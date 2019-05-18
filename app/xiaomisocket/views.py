# coding:utf8
from . import xiaomisocket


@xiaomisocket.route("/")
def index():
    return "<h1 style='color:green'>小米插排<h1>"
