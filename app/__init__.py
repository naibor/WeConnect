from flask import Flask
from flask_jwt_extended import JWTManager
app = Flask(__name__, instance_relative_config=True)
# Setup the Flask-JWT-Extended extension
jwt = JWTManager(app)
from app.auth.views import register
from app.businesses.views import create_business
