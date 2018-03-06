from flask import Flask

app = Flask(__name__, instance_relative_config=True)

from app.auth.views import register
from app.businesses.views import create_business
