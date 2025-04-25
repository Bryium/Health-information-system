from flask import Flask
from flask_migrate import Migrate
from models import db
from config import Config
import routes
from api import api_bp




def create_app():
    app = Flask(__name__)  
    app.config.from_object(Config)  
    db.init_app(app)  
    Migrate(app, db)  

    # Register the blueprint(for web routes)
    app.register_blueprint(routes.main_bp)

     # Register the API blueprint(for the API routes)
    app.register_blueprint(api_bp)

    return app  

# Entry point for running the Flask app
if __name__ == '__main__':
    app = create_app() 
    app.run(debug=True) 
