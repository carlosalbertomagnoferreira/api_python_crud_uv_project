# API Assíncrona com FastAPI, PostgreSQL e Alembic

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-lightblue)](https://fastapi.tiangolo.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Container-blue)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Production%20Ready-blue?logo=kubernetes)](https://kubernetes.io/)

Este projeto é uma API REST assíncrona construída com **FastAPI**, usando **SQLAlchemy Async** para interação com **PostgreSQL**. Possui **CRUD completo** para usuários, **migrations automatizadas** com Alembic e testes de integração rodando automaticamente em Docker e Kubernetes.

---

## 🧩 Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI** (assíncrono)
- **SQLAlchemy 2.0 (Async)**
- **PostgreSQL**
- **Alembic** (migrations)
- **uv** (gerenciador de dependências)
- **httpx** (teste automatizado do CRUD)
- **Swagger UI** (documentação automática)
- **Docker & Docker Compose & Kubernetes**

---

## 📂 Estrutura do Projeto

```

api_python_crud_uv_project/
│── alembic/                          # Diretório das migrations
│   └── versions/                     # Arquivos de migrations
│── alembic.ini                       # Configuração Alembic
│── main.py                           # API FastAPI
│── models.py                         # Models SQLAlchemy
│── entrypoint.sh                     # Script de inicialização do container
│── test\_api.py                      # Testes de integração do CRUD
│── Dockerfile                        # Construção da imagem docker
│── docker-compose.yml                # Orquestração local (app + db)
│── pyproject.toml                    # Gerenciamento de dependências (uv)
│── uv.lock                           # Lockfile das dependências
│── k8s/                              # Manifestos Kubernetes (deploy app e banco)

```

---

## ⚡ Funcionalidades

### CRUD de Usuários

| Método | Endpoint | Descrição |
|--------|---------|-----------|
| GET    | `/users` | Lista todos os usuários |
| POST   | `/users` | Cria um novo usuário |
| PUT    | `/users/{user_id}` | Atualiza usuário existente |
| DELETE | `/users/{user_id}` | Deleta usuário pelo ID |

### Testes Automatizados
- Criação de usuário válido
- Prevenção de e-mails duplicados
- Atualização válida e inválida
- Deleção de usuário e tentativa de deletar inexistente

---

## 🚀 Rodando o Projeto

### 1. Pré-requisitos

- Docker & Docker Compose instalados
- Python 3.11 (se rodar localmente sem Docker)

---

### 2. Subindo com Docker Compose

```bash
docker-compose up --build
```

Fluxo automático:

1. O PostgreSQL inicia e fica saudável
2. Alembic aplica migrations automaticamente
3. API FastAPI inicia
4. Testes do CRUD (`test_api.py`) rodam automaticamente
5. API permanece rodando em `http://localhost:8000`

---

### 3. Documentação Swagger

Acesse no navegador:

* Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
* ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

### 4. Rodando local sem Docker

1. Instale dependências:

```bash
uv add fastapi uvicorn sqlalchemy[asyncio] asyncpg alembic httpx
```

2. Aplicar migrations:

```bash
uv run alembic upgrade head
```

3. Rodar API:

```bash
uv run uvicorn main:app --reload
```

4. Testar CRUD:

```bash
uv run python test_api.py
```

## ☸️ Deploy no Kubernetes

Para rodar a aplicação em um cluster Kubernetes, utilize os manifestos disponíveis no diretório `k8s/`.

Exemplo de aplicação dos manifestos:

```bash
kubectl apply -f k8s/database.yaml
kubectl apply -f k8s/app_deploy.yaml
```

Isso irá provisionar o banco de dados PostgreSQL e a aplicação FastAPI no cluster. Certifique-se de ter um cluster Kubernetes configurado e o `kubectl` apontando para o contexto correto.

Você pode customizar os arquivos conforme sua necessidade (por exemplo, variáveis de ambiente, storage, etc).

---

## 🛠 Configuração do Banco

* Usuário: `user`
* Senha: `password`
* Banco: `meubanco`
* Host Docker: `db`
* Porta: `5432`

**Variável de ambiente:** `DATABASE_URL=postgresql+asyncpg://user:password@db:5432/meubanco`

---

## 🔧 Migrations com Alembic

* Gerar migration:

```bash
uv run alembic revision --autogenerate -m "mensagem"
```

* Aplicar migration:

```bash
uv run alembic upgrade head
```

---

## ✅ Testes Automatizados

* Todos os testes estão em `test_api.py`
* Rodam automaticamente no container via `entrypoint.sh`
* Validam criação, leitura, atualização e deleção de usuários, incluindo cenários de erro

---

## 📌 Observações

* API totalmente assíncrona com FastAPI + SQLAlchemy Async
* Docker + Docker Compose facilitam o deploy e execução
* Alembic gerencia versionamento do banco
* Testes automatizados garantem integridade do CRUD

---

Feito com ❤️ por \[Carlos Alberto Magno Ferreira]
