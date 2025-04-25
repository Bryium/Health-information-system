from flask import Flask
from flask_migrate import Migrate
from models import db
from config import Config
import routes
from api import api_bp
from flask_jwt_extended import JWTManager
from auth import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
Migrate(app, db)
JWTManager(app)

# Register Blueprints
app.register_blueprint(routes.main_bp)
app.register_blueprint(api_bp)
app.register_blueprint(auth_bp)


if __name__ == '__main__':
    app.run(debug=True)
