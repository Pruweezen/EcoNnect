from flask import Flask
from .routes import main_bp

def create_app(config_class=None):
    app = Flask(__name__)
    
    if config_class:
        app.config.from_object(config_class)
    
    app.register_blueprint(main_bp)  # register routes
    
    return app
