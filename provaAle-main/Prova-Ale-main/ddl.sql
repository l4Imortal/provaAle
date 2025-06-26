CREATE TABLE usuario (
    id SERIAL PRIMARY KEY,
    nome_usuario VARCHAR(80) UNIQUE NOT NULL,
    senha_hash VARCHAR(128) NOT NULL,
    tipo VARCHAR(20) NOT NULL
);

CREATE TABLE turma (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    professor_responsavel VARCHAR(100),
    horario VARCHAR(50)
);

CREATE TABLE aluno (
    id SERIAL PRIMARY KEY,
    nome_completo VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    contato VARCHAR(200),
    turma_id INTEGER REFERENCES turma(id)
);

CREATE TABLE pagamento (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER NOT NULL REFERENCES aluno(id),
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valor FLOAT NOT NULL,
    status VARCHAR(20) NOT NULL
);

CREATE TABLE presenca (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER NOT NULL REFERENCES aluno(id),
    data DATE NOT NULL,
    presente BOOLEAN NOT NULL
);

CREATE TABLE atividade (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(200) NOT NULL,
    data DATE NOT NULL,
    turma_id INTEGER NOT NULL REFERENCES turma(id)
);

CREATE TABLE atividade_aluno (
    id SERIAL PRIMARY KEY,
    atividade_id INTEGER NOT NULL REFERENCES atividade(id),
    aluno_id INTEGER NOT NULL REFERENCES aluno(id)
);