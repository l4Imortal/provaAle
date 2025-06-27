from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configurações do banco
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        'SQLALCHEMY_DATABASE_URI', 
        'postgresql://postgres:postgres@db:5432/schooldb'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev-secret-key'
    
    # Inicializar banco
    db.init_app(app)
    
    # Importar modelos
    from app.models import Turma, Student
    
    # Criar tabelas
    with app.app_context():
        db.create_all()
    
    # Rotas com banco real
    @app.route('/')
    def home():
        return jsonify({
            'message': 'API Sistema Escolar funcionando!', 
            'status': 'success',
            'database': 'PostgreSQL conectado'
        })
    
    @app.route('/health')
    def health():
        try:
            # Testar conexão com banco
            db.session.execute(text('SELECT 1'))
            return jsonify({'status': 'healthy', 'database': 'connected'})
        except Exception as e:
            return jsonify({'status': 'error', 'database': 'disconnected', 'error': str(e)}), 500
    
    @app.route('/turmas', methods=['GET'])
    def list_turmas():
        try:
            turmas = Turma.query.all()
            return jsonify([turma.to_dict() for turma in turmas])
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @app.route('/turmas', methods=['POST'])
    def create_turma():
        try:
            data = request.get_json()
            
            if not data or not data.get('nome'):
                return jsonify({'error': 'Nome é obrigatório'}), 400
            
            turma = Turma(
                nome=data.get('nome'),
                ano=data.get('ano', 2025)
            )
            
            db.session.add(turma)
            db.session.commit()
            
            return jsonify({
                'message': 'Turma criada com sucesso!',
                'turma': turma.to_dict()
            }), 201
            
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    @app.route('/students', methods=['GET'])
    def list_students():
        try:
            students = Student.query.all()
            return jsonify([student.to_dict() for student in students])
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    @app.route('/students', methods=['POST'])
    def create_student():
        try:
            data = request.get_json()
            
            if not data or not data.get('nome') or not data.get('email'):
                return jsonify({'error': 'Nome e email são obrigatórios'}), 400
            
            student = Student(
                nome=data.get('nome'),
                email=data.get('email'),
                turma_id=data.get('turma_id')
            )
            
            db.session.add(student)
            db.session.commit()
            
            return jsonify({
                'message': 'Estudante criado com sucesso!',
                'student': student.to_dict()
            }), 201
            
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    return app
