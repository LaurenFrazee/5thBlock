
import os
from flaskr.routes import main_bp
from flaskr.auth import auth_bp
from flask import Flask
from dotenv import load_dotenv

from .db import db
from .routes import main_bp

def create_app():
    load_dotenv()  # Load environment variables from .env file

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///fifthblock.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.secret_key = 'super-secret-key'
    
    # Initialize the database with the app
    db.init_app(app)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    
    @app.route("/")
    def index():
        return "5th block is running"
    
    @app.route("/test")
    def test():
        return "Phase 1 verification successful"
    
    


    return app