#!/bin/sh
set -e

echo "📌 Rodando migrations do Alembic..."
uv run alembic upgrade head

echo "🚀 Iniciando a API em background..."
uv run uvicorn main:app --host 0.0.0.0 --port 8000 &

# Espera a API subir
echo "⏳ Aguardando a API inicializar..."
sleep 5

echo "📌 Rodando testes do CRUD..."
uv run python test_api.py

# Mantém o container ativo
wait
