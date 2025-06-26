from flask import Blueprint, request, jsonify

attendance_bp = Blueprint('attendance', __name__)

@attendance_bp.route('/attendance', methods=['GET'])
def list_attendance():
    return jsonify([
        {'id': 1, 'aluno_id': 1, 'data': '2025-06-26', 'presente': True},
        {'id': 2, 'aluno_id': 2, 'data': '2025-06-26', 'presente': False}
    ])

@attendance_bp.route('/attendance', methods=['POST'])
def create_attendance():
    data = request.json
    return jsonify({
        'id': 3,
        'aluno_id': data.get('aluno_id'),
        'data': data.get('data'),
        'presente': data.get('presente'),
        'message': 'Presença registrada com sucesso!'
    }), 201
