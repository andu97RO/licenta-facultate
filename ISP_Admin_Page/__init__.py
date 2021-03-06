from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from time import sleep

db = SQLAlchemy()


def create_app():

    app = Flask(__name__, instance_relative_config=False)
    # app.config.from_object('config.Config')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    app.config['SECRET_KEY'] = 'CheieSecretaLicenta'

    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()

        return app
