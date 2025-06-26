from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_restx import Api
import os

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    
    # Configurações
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', 'sqlite:///escola.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-key')
    
    # Inicializar extensões
    db.init_app(app)
    jwt.init_app(app)
    
    # Configurar Flask-RESTX (Swagger)
    api = Api(app, 
              title='Sistema Escolar API',
              version='1.0',
              description='API para gerenciar escola',
              doc='/swagger/')
    
    # Registrar blueprints
    try:
        from app.routes.classes import classes_bp
        app.register_blueprint(classes_bp)
    except ImportError:
        pass
    
    try:
        from app.routes.students import students_bp
        app.register_blueprint(students_bp)
    except ImportError:
        pass
    
    try:
        from app.routes.payments import payments_bp
        app.register_blueprint(payments_bp)
    except ImportError:
        pass
    
    try:
        from app.routes.attendance import attendance_bp
        app.register_blueprint(attendance_bp)
    except ImportError:
        pass
    
    # Rota básica
    @app.route('/')
    def home():
        return {'message': 'API funcionando!', 'swagger': '/swagger/', 'status': 'success'}
    
    @app.route('/health')
    def health():
        return {'status': 'healthy'}
    
    return app
