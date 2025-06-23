from flask import Blueprint, request, jsonify
from app.models import db, Presenca

attendance_bp = Blueprint('attendance', __name__)

# Registrar presença
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

# Listar presenças de um aluno
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