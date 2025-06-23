from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    JWTManager(app)

    from .routes.auth import auth_bp
    from .routes.students import students_bp
    from .routes.payments import payments_bp
    from .routes.attendance import attendance_bp
    from .routes.activities import activities_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(students_bp)
    app.register_blueprint(payments_bp)
    app.register_blueprint(attendance_bp)
    app.register_blueprint(activities_bp)

    return app
