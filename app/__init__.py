from flask import Flask, jsonify
from .extensions import db, migrate

def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register blueprints
    from .lgu.controllers.lgu_controller import lgu_bp
    from .company.controllers.company_controller import company_bp
    from .jobseeker.controllers.jobseeker_controller import jobseeker_bp

    app.register_blueprint(lgu_bp, url_prefix="/lgu")
    app.register_blueprint(company_bp, url_prefix="/company")
    app.register_blueprint(jobseeker_bp, url_prefix="/jobseeker")

    @app.route("/")
    def home():
        return jsonify({"status": "EcoNnect API", "message": "running"})

    return app
