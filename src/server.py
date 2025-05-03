from flask import Flask
from routes.homeRoute import router
from config.config import Config
import os
from flask_cors import CORS

def createApp():
    app = Flask(__name__, static_url_path='/static', static_folder=os.path.join(os.path.dirname(__file__), 'static'))
    CORS(app)

    app.config.from_object(Config)
    os.makedirs(Config.INPUT_FOLDER, exist_ok=True)
    os.makedirs(Config.OUTPUT_FOLDER, exist_ok=True)

    app.register_blueprint(router, url_prefix='/api')

    return app