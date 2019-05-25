from flask import Blueprint

servocontrol = Blueprint("servocontrol", __name__)

import app.servocontrol.servo
