# 🏫 Sistema de Gestão Escolar Infantil

## 🎯 Objetivo
Consolidar os conhecimentos em ambientes de desenvolvimento e bancos de dados utilizando conteinerização, por meio da criação da infraestrutura de backend para um sistema de gestão de escola infantil.

---

## 📘 1. Contexto
Vocês são a equipe de backend responsável pela criação da infraestrutura de um sistema de gestão para uma escola infantil.

---

## 🎯 2. Objetivos do Sistema

- **Gerenciamento de Pagamentos:** Registro, acompanhamento e geração de relatórios de mensalidades e taxas.
- **Controle de Presenças:** Registro e consulta da frequência dos alunos, com relatórios.
- **Gerenciamento de Atividades:** Cadastro, organização e visualização das atividades pedagógicas.

---

## 📦 3. Escopo do Sistema

### 🔹 Módulo de Pagamentos
- Cadastro de alunos com dados financeiros.
- Registro de mensalidades, matrículas e taxas extras.
- Consulta de pagamentos pendentes e realizados.
- Geração de relatórios financeiros.

### 🔹 Módulo de Presenças
- Registro diário de presença dos alunos.
- Consulta por aluno/período.
- Geração de relatórios de frequência.

### 🔹 Módulo de Atividades
- Cadastro de atividades pedagógicas.
- Associação entre alunos e atividades.
- Visualização de atividades por aluno e por turma.

---

## ✅ 4. Requisitos Funcionais

- **RF001:** Autenticação de usuários com níveis de permissão.
- **RF002:** CRUD de alunos.
- **RF003:** Gerenciamento de turmas.
- **RF004:** Registro manual de pagamentos.
- **RF005:** Consulta de pagamentos por aluno, período e status.
- **RF006:** Geração de relatórios de pagamentos.
- **RF007:** Registro de presenças.
- **RF008:** Relatórios de presença.
- **RF009:** Cadastro e associação de atividades pedagógicas.
- **RF010:** Relatórios e visualização de atividades.

---

## 🧱 5. Requisitos Não Funcionais

- **RNF001:** Desempenho responsivo.
- **RNF002:** Interface intuitiva.
- **RNF003:** Segurança dos dados.
- **RNF004:** Alta disponibilidade.
- **RNF005:** Escalabilidade.
- **RNF006:** Código limpo e documentado.
- **RNF007:** Compatível com navegadores modernos.

---

## 🛠️ 6. Requisitos Técnicos

- **Linguagem:** Python  
- **Framework Web:** Flask  
- **Banco de Dados:** PostgreSQL  
- **Controle de Versão:** Git  
- **Testes:** Unitários e de integração  
- **Implantação:** Docker e AWS  
- **CI/CD:** GitHub Actions  

---

## 🗂️ 7. Estrutura do Projeto

```
📁 app/                # Código-fonte do backend
📄 ddl.sql             # Script de criação do banco de dados
🐳 Dockerfile          # Backend (Flask)
🐳 Dockerfile.db       # Banco de Dados (PostgreSQL)
🔧 docker-compose.yml  # Orquestração dos containers
📄 requirements.txt    # Dependências Python
```

---

## ▶️ 8. Passo a Passo para Execução

```bash
# 1. Clone o repositório
git clone https://github.com/seuusuario/seurepositorio.git

# 2. Acesse a pasta do projeto
cd seurepositorio

# 3. Configure as variáveis de ambiente
# Exemplo disponível em .env.example

# 4. Suba os containers
docker-compose up --build
```

- Backend disponível em: [http://localhost:5000](http://localhost:5000)  
- Banco de dados: porta **5432**

---

## 📊 9. Modelo Entidade-Relacionamento (MER)

O diagrama abaixo representa a estrutura conceitual das entidades e seus relacionamentos:

![MER do Sistema](./mer_diagrama.png)

---

## 📉 10. Diagrama Entidade-Relacionamento Lógico (DER)

O diagrama abaixo representa a estrutura lógica do banco de dados com seus relacionamentos:


---

## 🧪 11. Critérios de Aceitação

O sistema será aceito quando atender a **todos os requisitos funcionais e não funcionais**, validados por testes e pela equipe cliente.

---

## 🧾 Prova-Ale
