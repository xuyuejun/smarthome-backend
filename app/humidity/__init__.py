from flask import Blueprint

humidity = Blueprint("humidity", __name__)

import app.humidity.hygrometer
