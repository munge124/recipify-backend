from flask import Flask
from flask_cors import CORS
from server.models import db
from config import Config
from controllers.routes import init_routes
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    
    # Configure the database (SQLite example)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  

    # Initialize db with the Flask app
    db.init_app(app)
    db = SQLAlchemy(app)
    migrate = Migrate()

    # Create tables 
    with app.app_context():
        db.create_all()

    # Register blueprints or routes 
    app.register_blueprint(init_routes)

    return app

# Run the app
if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)