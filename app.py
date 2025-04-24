from flask import Flask
from flask_migrate import Migrate
from models import db
from config import Config
import routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    routes.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
