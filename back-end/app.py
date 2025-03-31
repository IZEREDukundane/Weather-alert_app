from flask import Flask
from flask_migrate import Migrate
from database import db
from routes import auth, alerts, users

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    
    # Initialize database
    db.init_app(app)
    migrate = Migrate(app, db)
    
    # Register routes
    app.register_blueprint(auth.bp)
    app.register_blueprint(alerts.bp)
    app.register_blueprint(users.bp)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
