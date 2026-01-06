
import os
from flask import Flask
from dotenv import load_dotenv
from .db import db

def create_app():
    load_dotenv()  # Load environment variables from .env file

    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///fifthblock.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize the database with the app
    db.init_app(app)
    
    @app.route("/")
    def index():
        return "5th block is running"

    return app