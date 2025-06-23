from flask import Blueprint, request, jsonify
from app.models import db, Turma

classes_bp = Blueprint('classes', __name__)

# Criar turma
@classes_bp.route('/turmas', methods=['POST'])
def criar_turma():
    dados = request.json
    turma = Turma(
        nome=dados['nome'],
        professor_responsavel=dados.get('professor_responsavel'),
        horario=dados.get('horario')
    )
    db.session.add(turma)
    db.session.commit()
    return jsonify({'mensagem': 'Turma criada com sucesso!'}), 201

# Listar turmas
@classes_bp.route('/turmas', methods=['GET'])
def listar_turmas():
    turmas = Turma.query.all()
    return jsonify([
        {
            'id': t.id,
            'nome': t.nome,
            'professor_responsavel': t.professor_responsavel,
            'horario': t.horario
        } for t in turmas
    ])

# Buscar turma por ID
@classes_bp.route('/turmas/<int:id>', methods=['GET'])
def buscar_turma(id):
    turma = Turma.query.get_or_404(id)
    return jsonify({
        'id': turma.id,
        'nome': turma.nome,
        'professor_responsavel': turma.professor_responsavel,
        'horario': turma.horario
    })

# Atualizar turma
@classes_bp.route('/turmas/<int:id>', methods=['PUT'])
def atualizar_turma(id):
    turma = Turma.query.get_or_404(id)
    dados = request.json
    turma.nome = dados.get('nome', turma.nome)
    turma.professor_responsavel = dados.get('professor_responsavel', turma.professor_responsavel)
    turma.horario = dados.get('horario', turma.horario)
    db.session.commit()
    return jsonify({'mensagem': 'Turma atualizada com sucesso!'})

# Excluir turma
@classes_bp.route('/turmas/<int:id>', methods=['DELETE'])
def excluir_turma(id):
    turma = Turma.query.get_or_404(id)
    db.session.delete(turma)
    db.session.commit()
    return jsonify({'mensagem': 'Turma excluída com sucesso!'})