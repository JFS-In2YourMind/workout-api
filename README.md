# 🏋 Workout API - FastAPI

API assíncrona para gerenciamento de atletas de academias de CrossFit, desenvolvida com **FastAPI**, **SQLAlchemy**, **PostgreSQL** e **AsyncPG**.

> 🔗 Projeto criado para o desafio da DIO (Digital Innovation One)

---

##  Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [AsyncPG](https://magicstack.github.io/asyncpg/)
- [FastAPI Pagination](https://fastapi-pagination.tkdodo.eu/)
- [Uvicorn](https://www.uvicorn.org/) (ASGI Server)

---

##  Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/JFS-In2YourMind/workout_api.git
cd workout_api
python -m venv .venv
2. Ative o ambiente virtual
python -m venv .venv
.\.venv\Scripts\activate

3. Instale as dependências
pip install -r requirements.txt

4. Configure o banco e crie as tabelas
python init_db.py


Certifique-se de que o PostgreSQL está rodando e que o banco workout_db existe.

5. Inicie o servidor
python run.py


Acesse: http://localhost:8000/docs

 Endpoints principais

POST /atletas → Cadastrar novo atleta

GET /atletas → Listar atletas (com filtros por nome/cpf e paginação)

Suporte a paginação com limit e offset

Tratamento de exceções com IntegrityError e status_code 303

 Funcionalidades extras

✅ Paginação com fastapi-pagination

✅ Filtros por nome e CPF via Query Params

✅ Mensagens de erro amigáveis para duplicação de CPF

✅ Estrutura modular com SQLAlchemy e routers

 Autor

Projeto desenvolvido por Jaqueline Felix

 | LinkedIn : https://www.linkedin.com/in/jaqueline-felix-7a05bb267/
