from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.models import db, Usuario

auth_bp = Blueprint('auth', __name__)

# Cadastro de usuário
@auth_bp.route('/usuarios', methods=['POST'])
def cadastrar_usuario():
    dados = request.json
    if Usuario.query.filter_by(nome_usuario=dados['nome_usuario']).first():
        return jsonify({'msg': 'Usuário já existe!'}), 400
    usuario = Usuario(
        nome_usuario=dados['nome_usuario'],
        tipo=dados['tipo']
    )
    usuario.set_senha(dados['senha'])
    db.session.add(usuario)
    db.session.commit()
    return jsonify({'msg': 'Usuário cadastrado com sucesso!'}), 201

# Login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = Usuario.query.filter_by(nome_usuario=data['nome_usuario']).first()
    if usuario and usuario.check_senha(data['senha']):
        token = create_access_token(identity={'id': usuario.id, 'tipo': usuario.tipo})
        return jsonify(access_token=token), 200
    return jsonify(msg='Credenciais inválidas'), 401