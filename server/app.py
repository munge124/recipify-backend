from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from server.config import Config
from server.models import db
from server.controllers.routes import init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load config from class

    db.init_app(app)
    migrate = Migrate(app, db)  # <-- PASS db here

    CORS(app)  # Optional: allow frontend to access

    with app.app_context():
        db.create_all()

    app.register_blueprint(init_routes)

    

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
