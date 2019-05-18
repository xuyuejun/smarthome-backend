from flask import Flask

app = Flask(__name__)
app.debug = True

from app.xiaomisocket import xiaomisocket as home_blueprint
from app.temperature import temperature as admin_blueprint

app.register_blueprint(home_blueprint, url_prefix="/socket")
app.register_blueprint(admin_blueprint, url_prefix="/temp")
