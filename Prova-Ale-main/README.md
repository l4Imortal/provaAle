# Sistema de Gestão Escolar Infantil

## Objetivo

Consolidar os conhecimentos em ambientes de desenvolvimento e bancos de dados utilizando conteinerização, por meio da criação da infraestrutura de backend para um sistema de gestão de escola infantil.

---

## 1. Contexto

Vocês são a equipe de backend responsável pela criação da infraestrutura de um sistema de gestão para uma escola infantil.

---

## 2. Objetivos do Sistema

- **Gerenciamento de Pagamentos:** Registro, acompanhamento e geração de relatórios de pagamentos de mensalidades e taxas escolares.
- **Controle de Presenças:** Registro e acompanhamento da frequência dos alunos, com geração de relatórios.
- **Gerenciamento de Atividades:** Cadastro, organização e visualização das atividades pedagógicas realizadas com os alunos.

---

## 3. Escopo do Sistema

### Módulo de Pagamentos
- Cadastro de alunos com informações financeiras.
- Registro de pagamentos (mensalidades, matrículas, taxas extras).
- Acompanhamento de pagamentos pendentes e realizados.
- Geração de relatórios financeiros.

### Módulo de Presenças
- Registro diário de presença dos alunos.
- Visualização da frequência por aluno e por período.
- Geração de relatórios de frequência.

### Módulo de Atividades
- Cadastro de atividades pedagógicas.
- Associação de atividades aos alunos.
- Visualização das atividades por aluno e por turma.

---

## 4. Requisitos Funcionais

- **RF001:** Autenticação de usuários com diferentes níveis de permissão.
- **RF002:** Gerenciamento completo de alunos.
- **RF003:** Gerenciamento de turmas.
- **RF004:** Registro manual de pagamentos.
- **RF005:** Consulta de pagamentos por aluno, período e status.
- **RF006:** Geração de relatórios de pagamentos.
- **RF007:** Registro de presenças.
- **RF008:** Consulta e geração de relatórios de presenças.
- **RF009:** Cadastro e associação de atividades pedagógicas.
- **RF010:** Visualização e relatórios de atividades.

---

## 5. Requisitos Não Funcionais

- **RNF001:** Desempenho responsivo.
- **RNF002:** Usabilidade intuitiva.
- **RNF003:** Segurança dos dados.
- **RNF004:** Alta disponibilidade e confiabilidade.
- **RNF005:** Escalabilidade.
- **RNF006:** Código organizado e documentado.
- **RNF007:** Compatibilidade com navegadores modernos.

---

## 6. Requisitos Técnicos

- **Linguagem:** Python
- **Framework Web:** Flask
- **Banco de Dados:** PostgreSQL
- **Controle de Versão:** Git
- **Testes:** Unitários e de integração
- **Implantação:** Docker e AWS
- **CI/CD:** GitHub Actions

---

## 7. Estrutura do Projeto

- `ddl.sql`: Script de criação do banco de dados.
- `Dockerfile.db`: Dockerfile para o banco de dados PostgreSQL.
- `Dockerfile`: Dockerfile para o backend Flask.
- `docker-compose.yml`: Orquestração dos containers.
- `app/`: Código-fonte do backend.
- `requirements.txt`: Dependências Python.

---

## 8. Passo a Passo para Execução

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/seurepositorio.git
   cd seurepositorio
   ```

2. **Configure as variáveis de ambiente no arquivo `.env`**  
   (Exemplo disponível como `.env.example`).

3. **Suba os containers:**
   ```bash
   docker-compose up --build
   ```

4. **Acesse o sistema:**
   - Backend: [http://localhost:5000](http://localhost:5000)
   - Banco de dados: porta 5432

---

## 9. Critérios de Aceitação

O sistema será aceito quando atender a todos os requisitos funcionais e não funcionais, validados por testes e pelo cliente.

---

## 10. Próximos Passos

- Reunião com o cliente para validação e refinamento dos requisitos.
- Construção do MER e DER.
- Definição da arquitetura e tecnologias específicas.
- Elaboração de cronograma detalhado e proposta comercial.

---

# Prova-Ale