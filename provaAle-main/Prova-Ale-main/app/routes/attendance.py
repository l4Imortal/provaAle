from flask import Blueprint, request, jsonify
from app.models import db, Presenca

attendance_bp = Blueprint('attendance', __name__)

# CREATE - Registrar presença
@attendance_bp.route('/presencas', methods=['POST'])
def registrar_presenca():
    dados = request.json
    presenca = Presenca(
        aluno_id=dados['aluno_id'],
        data=dados['data'],
        presente=dados['presente']
    )
    db.session.add(presenca)
    db.session.commit()
    return jsonify({'mensagem': 'Presença registrada com sucesso!'}), 201

# READ - Listar presenças de um aluno
@attendance_bp.route('/presencas/<int:aluno_id>', methods=['GET'])
def listar_presencas(aluno_id):
    presencas = Presenca.query.filter_by(aluno_id=aluno_id).all()
    return jsonify([
        {
            'id': p.id,
            'data': p.data.strftime('%Y-%m-%d'),
            'presente': p.presente
        } for p in presencas
    ])

# READ - Buscar presença específica
@attendance_bp.route('/presencas/detalhes/<int:presenca_id>', methods=['GET'])
def buscar_presenca(presenca_id):
    presenca = Presenca.query.get_or_404(presenca_id)
    return jsonify({
        'id': presenca.id,
        'aluno_id': presenca.aluno_id,
        'data': presenca.data.strftime('%Y-%m-%d'),
        'presente': presenca.presente
    })

# UPDATE - Atualizar presença
@attendance_bp.route('/presencas/<int:presenca_id>', methods=['PUT'])
def atualizar_presenca(presenca_id):
    presenca = Presenca.query.get_or_404(presenca_id)
    dados = request.json
    
    presenca.presente = dados.get('presente', presenca.presente)
    presenca.data = dados.get('data', presenca.data)
    
    db.session.commit()
    return jsonify({'mensagem': 'Presença atualizada com sucesso!'})

# DELETE - Deletar presença
@attendance_bp.route('/presencas/<int:presenca_id>', methods=['DELETE'])
def deletar_presenca(presenca_id):
    presenca = Presenca.query.get_or_404(presenca_id)
    db.session.delete(presenca)
    db.session.commit()
    return jsonify({'mensagem': 'Presença deletada com sucesso!'})

# EXTRA - Listar presenças por data
@attendance_bp.route('/presencas/data/<string:data>', methods=['GET'])
def listar_presencas_por_data(data):
    presencas = Presenca.query.filter_by(data=data).all()
    return jsonify([
        {
            'id': p.id,
            'aluno_id': p.aluno_id,
            'presente': p.presente
        } for p in presencas
    ])
