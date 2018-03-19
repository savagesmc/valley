from flask import Blueprint
songs = Blueprint('songs', __name__)
from . import views, errors
