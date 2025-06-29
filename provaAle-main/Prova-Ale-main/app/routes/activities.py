from flask import Blueprint, request, jsonify
from app.models import db, Atividade, AtividadeAluno

activities_bp = Blueprint('activities', __name__)

# CREATE - Cadastrar atividade
@activities_bp.route('/atividades', methods=['POST'])
def cadastrar_atividade():
    dados = request.json
    atividade = Atividade(
        descricao=dados['descricao'],
        data=dados['data'],
        turma_id=dados['turma_id']
    )
    db.session.add(atividade)
    db.session.commit()
    return jsonify({'mensagem': 'Atividade cadastrada com sucesso!'}), 201

# READ - Listar atividades de uma turma
@activities_bp.route('/atividades/turma/<int:turma_id>', methods=['GET'])
def listar_atividades_turma(turma_id):
    atividades = Atividade.query.filter_by(turma_id=turma_id).all()
    return jsonify([
        {
            'id': a.id,
            'descricao': a.descricao,
            'data': a.data.strftime('%Y-%m-%d')
        } for a in atividades
    ])

# UPDATE - Atualizar atividade
@activities_bp.route('/atividades/<int:atividade_id>', methods=['PUT'])
def atualizar_atividade(atividade_id):
    atividade = Atividade.query.get_or_404(atividade_id)
    dados = request.json
    
    atividade.descricao = dados.get('descricao', atividade.descricao)
    atividade.data = dados.get('data', atividade.data)
    atividade.turma_id = dados.get('turma_id', atividade.turma_id)
    
    db.session.commit()
    return jsonify({'mensagem': 'Atividade atualizada com sucesso!'})

# DELETE - Deletar atividade
@activities_bp.route('/atividades/<int:atividade_id>', methods=['DELETE'])
def deletar_atividade(atividade_id):
    atividade = Atividade.query.get_or_404(atividade_id)
    db.session.delete(atividade)
    db.session.commit()
    return jsonify({'mensagem': 'Atividade deletada com sucesso!'})

# Associar atividade a aluno
@activities_bp.route('/atividades/<int:atividade_id>/aluno', methods=['POST'])
def associar_atividade_aluno(atividade_id):
    dados = request.json
    atividade_aluno = AtividadeAluno(
        atividade_id=atividade_id,
        aluno_id=dados['aluno_id']
    )
    db.session.add(atividade_aluno)
    db.session.commit()
    return jsonify({'mensagem': 'Atividade associada ao aluno com sucesso!'}), 201

# Listar atividades de um aluno
@activities_bp.route('/atividades/aluno/<int:aluno_id>', methods=['GET'])
def listar_atividades_aluno(aluno_id):
    atividades_aluno = AtividadeAluno.query.filter_by(aluno_id=aluno_id).all()
    return jsonify([
        {
            'atividade_id': aa.atividade_id,
            'descricao': aa.atividade.descricao,
            'data': aa.atividade.data.strftime('%Y-%m-%d')
        } for aa in atividades_aluno
    ])
