from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.debug = True
CORS(app, supports_credentials=True)

from app.temperature import temperature as temp_blueprint
from app.xiaomisocket import xiaomisocket as socket_blueprint
from app.testpage import testpage as test_blueprint
from app.humidity import humidity as humidity_blueprint

app.register_blueprint(temp_blueprint, url_prefix="/temp")
app.register_blueprint(socket_blueprint, url_prefix="/socket")
app.register_blueprint(test_blueprint, url_prefix="/test")
app.register_blueprint(test_blueprint, url_prefix="/hygrometer")