from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Student

students_bp = Blueprint('students', __name__)

# CREATE - Criar estudante
@students_bp.route('/students', methods=['POST'])
@jwt_required()
def create_student():
    current_user = get_jwt_identity()
    if current_user['tipo'] not in ['admin', 'professor']:
        return jsonify({'msg': 'Acesso negado'}), 403
    
    data = request.json
    
    # Validações básicas
    required_fields = ['nome', 'email']
    for field in required_fields:
        if field not in data or not data[field]:
            return jsonify({'msg': f'Campo {field} é obrigatório'}), 400
    
    # Verificar se email já existe
    if Student.query.filter_by(email=data['email']).first():
        return jsonify({'msg': 'Email já cadastrado'}), 400
    
    try:
        student = Student(**data)
        db.session.add(student)
        db.session.commit()
        return jsonify({
            'id': student.id,
            'mensagem': 'Estudante criado com sucesso!'
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'Erro ao criar estudante'}), 500

# READ - Listar todos os estudantes
@students_bp.route('/students', methods=['GET'])
@jwt_required()
def list_students():
    students = Student.query.all()
    return jsonify([
        {
            'id': s.id,
            'nome': s.nome,
            'email': s.email,
            'telefone': s.telefone if hasattr(s, 'telefone') else None,
            'turma_id': s.turma_id if hasattr(s, 'turma_id') else None,
            'data_nascimento': s.data_nascimento.strftime('%Y-%m-%d') if hasattr(s, 'data_nascimento') and s.data_nascimento else None
        } for s in students
    ])

# READ - Buscar estudante específico
@students_bp.route('/students/<int:student_id>', methods=['GET'])
@jwt_required()
def get_student(student_id):
    student = Student.query.get_or_404(student_id)
    return jsonify({
        'id': student.id,
        'nome': student.nome,
        'email': student.email,
        'telefone': student.telefone if hasattr(student, 'telefone') else None,
        'turma_id': student.turma_id if hasattr(student, 'turma_id') else None,
        'data_nascimento': student.data_nascimento.strftime('%Y-%m-%d') if hasattr(student, 'data_nascimento') and student.data_nascimento else None,
        'endereco': student.endereco if hasattr(student, 'endereco') else None
    })

# READ - Buscar estudantes por turma
@students_bp.route('/students/turma/<int:turma_id>', methods=['GET'])
@jwt_required()
def list_students_by_class(turma_id):
    students = Student.query.filter_by(turma_id=turma_id).all() if hasattr(Student, 'turma_id') else []
    return jsonify([
        {
            'id': s.id,
            'nome': s.nome,
            'email': s.email,
            'telefone': s.telefone if hasattr(s, 'telefone') else None
        } for s in students
    ])

# UPDATE - Atualizar estudante
@students_bp.route('/students/<int:student_id>', methods=['PUT'])
@jwt_required()
def update_student(student_id):
    current_user = get_jwt_identity()
    if current_user['tipo'] not in ['admin', 'professor']:
        return jsonify({'msg': 'Acesso negado'}), 403
    
    student = Student.query.get_or_404(student_id)
    data = request.json
    
    # Verificar se novo email já existe (se estiver sendo alterado)
    if 'email' in data and data['email'] != student.email:
        if Student.query.filter_by(email=data['email']).first():
            return jsonify({'msg': 'Email já cadastrado'}), 400
    
    # Atualizar campos
    if 'nome' in data:
        student.nome = data['nome']
    if 'email' in data:
        student.email = data['email']
    if 'telefone' in data and hasattr(student, 'telefone'):
        student.telefone = data['telefone']
    if 'turma_id' in data and hasattr(student, 'turma_id'):
        student.turma_id = data['turma_id']
    if 'data_nascimento' in data and hasattr(student, 'data_nascimento'):
        student.data_nascimento = data['data_nascimento']
    if 'endereco' in data and hasattr(student, 'endereco'):
        student.endereco = data['endereco']
    
    try:
        db.session.commit()
        return jsonify({'mensagem': 'Estudante atualizado com sucesso!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'Erro ao atualizar estudante'}), 500

# DELETE - Deletar estudante
@students_bp.route('/students/<int:student_id>', methods=['DELETE'])
@jwt_required()
def delete_student(student_id):
    current_user = get_jwt_identity()
    if current_user['tipo'] != 'admin':
        return jsonify({'msg': 'Apenas administradores podem deletar estudantes'}), 403
    
    student = Student.query.get_or_404(student_id)
    
    try:
        db.session.delete(student)
        db.session.commit()
        return jsonify({'mensagem': 'Estudante deletado com sucesso!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'Erro ao deletar estudante'}), 500

# EXTRA - Buscar estudante por email
@students_bp.route('/students/email/<string:email>', methods=['GET'])
@jwt_required()
def get_student_by_email(email):
    student = Student.query.filter_by(email=email).first_or_404()
    return jsonify({
        'id': student.id,
        'nome': student.nome,
        'email': student.email,
        'telefone': student.telefone if hasattr(student, 'telefone') else None,
        'turma_id': student.turma_id if hasattr(student, 'turma_id') else None
    })

# EXTRA - Contar estudantes
@students_bp.route('/students/count', methods=['GET'])
@jwt_required()
def count_students():
    total = Student.query.count()
    return jsonify({'total_estudantes': total})

# EXTRA - Transferir estudante de turma
@students_bp.route('/students/<int:student_id>/transferir', methods=['PATCH'])
@jwt_required()
def transfer_student(student_id):
    current_user = get_jwt_identity()
    if current_user['tipo'] not in ['admin', 'professor']:
        return jsonify({'msg': 'Acesso negado'}), 403
    
    student = Student.query.get_or_404(student_id)
    data = request.json
    
    if 'nova_turma_id' not in data:
        return jsonify({'msg': 'nova_turma_id é obrigatório'}), 400
    
    if hasattr(student, 'turma_id'):
        student.turma_id = data['nova_turma_id']
        db.session.commit()
        return jsonify({'mensagem': 'Estudante transferido com sucesso!'})
    else:
        return jsonify({'msg': 'Funcionalidade não disponível'}), 400
