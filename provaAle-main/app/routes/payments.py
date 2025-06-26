from flask import Blueprint, request, jsonify

payments_bp = Blueprint('payments', __name__)

@payments_bp.route('/payments', methods=['GET'])
def list_payments():
    return jsonify([
        {'id': 1, 'aluno_id': 1, 'valor': 150.00, 'status': 'pago'},
        {'id': 2, 'aluno_id': 2, 'valor': 150.00, 'status': 'pendente'}
    ])

@payments_bp.route('/payments', methods=['POST'])
def create_payment():
    data = request.json
    return jsonify({
        'id': 3,
        'aluno_id': data.get('aluno_id'),
        'valor': data.get('valor'),
        'status': 'pendente',
        'message': 'Pagamento criado com sucesso!'
    }), 201
