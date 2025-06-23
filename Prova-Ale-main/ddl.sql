CREATE TABLE aluno (
    id SERIAL PRIMARY KEY,
    nome_completo VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    contato VARCHAR(200)
);

CREATE TABLE pagamento (
    id SERIAL PRIMARY KEY,
    aluno_id INTEGER NOT NULL REFERENCES aluno(id),
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valor FLOAT NOT NULL,
    status VARCHAR(20) NOT NULL
);