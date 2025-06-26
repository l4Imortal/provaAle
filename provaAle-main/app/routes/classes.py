from flask import Blueprint, request, jsonify

classes_bp = Blueprint('classes', __name__)

@classes_bp.route('/turmas', methods=['GET'])
def list_classes():
    return jsonify([
        {'id': 1, 'nome': 'Turma A', 'ano': 2025},
        {'id': 2, 'nome': 'Turma B', 'ano': 2025}
    ])

@classes_bp.route('/turmas', methods=['POST'])
def create_class():
    data = request.json
    return jsonify({
        'id': 3, 
        'nome': data.get('nome'), 
        'message': 'Turma criada com sucesso!'
    }), 201
