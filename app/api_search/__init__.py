from flask import Blueprint

api_search = Blueprint('api_search', __name__)

from . import views, errors
