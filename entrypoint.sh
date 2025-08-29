#!/bin/sh
set -e

echo "📌 Rodando migrations do Alembic..."
uv run alembic upgrade head

echo "🚀 Iniciando a API..."
exec uv run uvicorn main:app --host 0.0.0.0 --port 8000
