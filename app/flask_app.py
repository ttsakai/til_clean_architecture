from flask import Flask
from app.rest import user
from app.flask_config import DevConfig

def create_app(config_object = DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(user.blueprint)
    return app


