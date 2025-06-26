from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, Payment

payments_bp = Blueprint('payments', __name__)

# CREATE - Criar pagamento
@payments_bp.route('/payments', methods=['POST'])
@jwt_required()
def create_payment():
    current_user = get_jwt_identity()
    if current_user['tipo'] not in ['admin', 'financeiro']:
        return jsonify({'msg': 'Acesso negado'}), 403
    
    data = request.json
    
    # Validações básicas
    required_fields = ['aluno_id', 'valor', 'data_vencimento']
    for field in required_fields:
        if field not in data:
            return jsonify({'msg': f'Campo {field} é obrigatório'}), 400
    
    try:
        payment = Payment(**data)
        db.session.add(payment)
        db.session.commit()
        return jsonify({
            'id': payment.id,
            'mensagem': 'Pagamento criado com sucesso!'
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'Erro ao criar pagamento'}), 500

# READ - Listar todos os pagamentos
@payments_bp.route('/payments', methods=['GET'])
@jwt_required()
def list_payments():
    current_user = get_jwt_identity()
    if current_user['tipo'] not in ['admin', 'financeiro']:
        return jsonify({'msg': 'Acesso negado'}), 403
    
    payments = Payment.query.all()
    return jsonify([
        {
            'id': p.id,
            'aluno_id': p.aluno_id,
            'valor': float(p.valor) if p.valor else 0,
            'data_vencimento': p.data_vencimento.strftime('%Y-%m-%d') if p.data_vencimento else None,
            'data_pagamento': p.data_pagamento.strftime('%Y-%m-%d') if p.data_pagamento else None,
            'status': p.status if hasattr(p, 'status') else 'pendente'
        } for p in payments
    ])

# READ - Buscar pagamento específico
@payments_bp.route('/payments/<int:payment_id>', methods=['GET'])
@jwt_required()
def get_payment(payment_id):
    current_user = get_jwt_identity()
    if current_user['tipo'] not in ['admin', 'financeiro']:
        return jsonify({'msg': 'Acesso negado'}), 403
    
    payment = Payment.query.get_or_404(payment_id)
    return jsonify({
        'id': payment.id,
        'aluno_id': payment.aluno_id,
        'valor': float(payment.valor) if payment.valor else 0,
        'data_vencimento': payment.data_vencimento.strftime('%Y-%m-%d') if payment.data_vencimento else None,
        'data_pagamento': payment.data_pagamento.strftime('%Y-%m-%d') if payment.data_pagamento else None,
        'status': payment.status if hasattr(payment, 'status') else 'pendente'
    })

# READ - Listar pagamentos por aluno
@payments_bp.route('/payments/aluno/<int:aluno_id>', methods=['GET'])
@jwt_required()
def list_payments_by_student(aluno_id):
    payments = Payment.query.filter_by(aluno_id=aluno_id).all()
    return jsonify([
        {
            'id': p.id,
            'valor': float(p.valor) if p.valor else 0,
            'data_vencimento': p.data_vencimento.strftime('%Y-%m-%d') if p.data_vencimento else None,
            'data_pagamento': p.data_pagamento.strftime('%Y-%m-%d') if p.data_pagamento else None,
            'status': p.status if hasattr(p, 'status') else 'pendente'
        } for p in payments
    ])

# UPDATE - Atualizar pagamento
@payments_bp.route('/payments/<int:payment_id>', methods=['PUT'])
@jwt_required()
def update_payment(payment_id):
    current_user = get_jwt_identity()
    if current_user['tipo'] not in ['admin', 'financeiro']:
        return jsonify({'msg': 'Acesso negado'}), 403
    
    payment = Payment.query.get_or_404(payment_id)
    data = request.json
    
    # Atualizar campos permitidos
    if 'valor' in data:
        payment.valor = data['valor']
    if 'data_vencimento' in data:
        payment.data_vencimento = data['data_vencimento']
    if 'data_pagamento' in data:
        payment.data_pagamento = data['data_pagamento']
    if 'status' in data and hasattr(payment, 'status'):
        payment.status = data['status']
    
    try:
        db.session.commit()
        return jsonify({'mensagem': 'Pagamento atualizado com sucesso!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'Erro ao atualizar pagamento'}), 500

# DELETE - Deletar pagamento
@payments_bp.route('/payments/<int:payment_id>', methods=['DELETE'])
@jwt_required()
def delete_payment(payment_id):
    current_user = get_jwt_identity()
    if current_user['tipo'] != 'admin':
        return jsonify({'msg': 'Apenas administradores podem deletar pagamentos'}), 403
    
    payment = Payment.query.get_or_404(payment_id)
    
    try:
        db.session.delete(payment)
        db.session.commit()
        return jsonify({'mensagem': 'Pagamento deletado com sucesso!'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'msg': 'Erro ao deletar pagamento'}), 500

# EXTRA - Marcar pagamento como pago
@payments_bp.route('/payments/<int:payment_id>/pagar', methods=['PATCH'])
@jwt_required()
def mark_as_paid(payment_id):
    current_user = get_jwt_identity()
    if current_user['tipo'] not in ['admin', 'financeiro']:
        return jsonify({'msg': 'Acesso negado'}), 403
    
    payment = Payment.query.get_or_404(payment_id)
    data = request.json
    
    payment.data_pagamento = data.get('data_pagamento')
    if hasattr(payment, 'status'):
        payment.status = 'pago'
    
    db.session.commit()
    return jsonify({'mensagem': 'Pagamento marcado como pago!'})
