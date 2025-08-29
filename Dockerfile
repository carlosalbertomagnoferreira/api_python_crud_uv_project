# Imagem base do Python
FROM python:3.11-slim

# Instala uv (gestor de dependências)
RUN pip install uv

# Define diretório de trabalho
WORKDIR /app

# Copia arquivos do projeto
COPY . .

# Instala dependências do pyproject.toml
RUN uv sync --frozen

# Expõe porta da API
EXPOSE 8000

# Comando padrão: entrypoint
CMD ["./entrypoint.sh"]
