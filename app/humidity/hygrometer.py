from . import humidity


@humidity.route("/")
def index():
    return "<h1 style='color:red'>湿度计<h1>"
