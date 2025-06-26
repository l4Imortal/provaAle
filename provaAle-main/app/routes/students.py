from flask import Blueprint, request, jsonify

students_bp = Blueprint('students', __name__)

@students_bp.route('/students', methods=['GET'])
def list_students():
    return jsonify([
        {'id': 1, 'nome': 'João Silva', 'email': 'joao@email.com'},
        {'id': 2, 'nome': 'Maria Santos', 'email': 'maria@email.com'}
    ])

@students_bp.route('/students', methods=['POST'])
def create_student():
    data = request.json
    return jsonify({
        'id': 3,
        'nome': data.get('nome'),
        'email': data.get('email'),
        'message': 'Estudante criado com sucesso!'
    }), 201
