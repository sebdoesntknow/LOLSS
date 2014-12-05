from flask import Blueprint

streams = Blueprint('streams', __name__)

from . import views, errors
