from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Usuário do sistema (admin, secretaria, professor)
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_usuario = db.Column(db.String(80), unique=True, nullable=False)
    senha_hash = db.Column(db.String(128), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)  # admin, secretaria, professor

    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def check_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

# Turma
class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    professor_responsavel = db.Column(db.String(100))
    horario = db.Column(db.String(50))
    alunos = db.relationship('Aluno', backref='turma', lazy=True)
    atividades = db.relationship('Atividade', backref='turma', lazy=True)

# Aluno
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_completo = db.Column(db.String(100), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=False)
    contato = db.Column(db.String(200))
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'))
    pagamentos = db.relationship('Pagamento', backref='aluno', lazy=True)
    presencas = db.relationship('Presenca', backref='aluno', lazy=True)
    atividades = db.relationship('AtividadeAluno', backref='aluno', lazy=True)

# Pagamento
class Pagamento(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)
    valor = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

# Presença
class Presenca(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    data = db.Column(db.Date, nullable=False)
    presente = db.Column(db.Boolean, nullable=False)

# Atividade pedagógica
class Atividade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    data = db.Column(db.Date, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turma.id'), nullable=False)
    alunos = db.relationship('AtividadeAluno', backref='atividade', lazy=True)

# Associação entre atividade e aluno (para saber quem participou de qual atividade)
class AtividadeAluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    atividade_id = db.Column(db.Integer, db.ForeignKey('atividade.id'), nullable=False)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.id'), nullable=False)
    # Se quiser, pode adicionar campos como "anexo" para arquivos, fotos, etc.