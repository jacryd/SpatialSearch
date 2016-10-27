# -*- coding: utf-8 -*-
import os
from flask import Flask
from server.api import api
from flask_cors import CORS, cross_origin

def create_app(settings_overrides=None):
	app = Flask(__name__)
	cors = CORS(app, resources={r"/*": {"origins": "*"}})
	configure_settings(app, settings_overrides)
	configure_blueprints(app)
	return app

def dbContext():
	conn = sqlite3.connect('searcher.db')
	db = c.conn.cursor()
	return db
	
	
def configure_settings(app, settings_override):
    parent = os.path.dirname(__file__)
    data_path = os.path.join(parent, '..', 'data')
    app.config.update({
        'DEBUG': True,
        'TESTING': False,
        'DATA_PATH': data_path
    })
    if settings_override:
        app.config.update(settings_override)


def configure_blueprints(app):
    app.register_blueprint(api)
