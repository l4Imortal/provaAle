from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import db, Usuario

auth_bp = Blueprint('auth', __name__)

# CREATE - Cadastro de usuário
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

# READ - Listar todos os usuários
@auth_bp.route('/usuarios', methods=['GET'])
@jwt_required()
def listar_usuarios():
    current_user = get_jwt_identity()
    if current_user['tipo'] != 'admin':
        return jsonify({'msg': 'Acesso negado'}), 403
    
    usuarios = Usuario.query.all()
    return jsonify([
        {
            'id': u.id,
            'nome_usuario': u.nome_usuario,
            'tipo': u.tipo
        } for u in usuarios
    ])

# READ - Buscar usuário específico
@auth_bp.route('/usuarios/<int:usuario_id>', methods=['GET'])
@jwt_required()
def buscar_usuario(usuario_id):
    current_user = get_jwt_identity()
    if current_user['tipo'] != 'admin' and current_user['id'] != usuario_id:
        return jsonify({'msg': 'Acesso negado'}), 403
    
    usuario = Usuario.query.get_or_404(usuario_id)
    return jsonify({
        'id': usuario.id,
        'nome_usuario': usuario.nome_usuario,
        'tipo': usuario.tipo
    })

# UPDATE - Atualizar usuário
@auth_bp.route('/usuarios/<int:usuario_id>', methods=['PUT'])
@jwt_required()
def atualizar_usuario(usuario_id):
    current_user = get_jwt_identity()
    if current_user['tipo'] != 'admin' and current_user['id'] != usuario_id:
        return jsonify({'msg': 'Acesso negado'}), 403
    
    usuario = Usuario.query.get_or_404(usuario_id)
    dados = request.json
    
    # Verificar se novo nome de usuário já existe
    if 'nome_usuario' in dados and dados['nome_usuario'] != usuario.nome_usuario:
        if Usuario.query.filter_by(nome_usuario=dados['nome_usuario']).first():
            return jsonify({'msg': 'Nome de usuário já existe!'}), 400
        usuario.nome_usuario = dados['nome_usuario']
    
    if 'tipo' in dados and current_user['tipo'] == 'admin':
        usuario.tipo = dados['tipo']
    
    if 'senha' in dados:
        usuario.set_senha(dados['senha'])
    
    db.session.commit()
    return jsonify({'msg': 'Usuário atualizado com sucesso!'})

# DELETE - Deletar usuário
@auth_bp.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
@jwt_required()
def deletar_usuario(usuario_id):
    current_user = get_jwt_identity()
    if current_user['tipo'] != 'admin':
        return jsonify({'msg': 'Acesso negado'}), 403
    
    usuario = Usuario.query.get_or_404(usuario_id)
    db.session.delete(usuario)
    db.session.commit()
    return jsonify({'msg': 'Usuário deletado com sucesso!'})

# Login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    usuario = Usuario.query.filter_by(nome_usuario=data['nome_usuario']).first()
    
    if usuario and usuario.check_senha(data['senha']):
        token = create_access_token(identity={'id': usuario.id, 'tipo': usuario.tipo})
        return jsonify(access_token=token), 200
    
    return jsonify(msg='Credenciais inválidas'), 401

# Perfil do usuário logado
@auth_bp.route('/perfil', methods=['GET'])
@jwt_required()
def perfil():
    current_user = get_jwt_identity()
    usuario = Usuario.query.get(current_user['id'])
    return jsonify({
        'id': usuario.id,
        'nome_usuario': usuario.nome_usuario,
        'tipo': usuario.tipo
    })
