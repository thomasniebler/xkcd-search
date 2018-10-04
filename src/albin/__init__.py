from flask import Flask

albin = Flask(__name__)

from .views import *
