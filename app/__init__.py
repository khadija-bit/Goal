from flask import Flask
from config import Config_options
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(__name__)

    # Setting up configuration
    app.config.from_object(config_options[config_name])
    

    #Initializing Flask Extensions
    bootstrap = Bootstrap(app)

    return app