# coding:utf8
from flask import Blueprint

temperature = Blueprint("temperature", __name__)

import app.temperature.views
