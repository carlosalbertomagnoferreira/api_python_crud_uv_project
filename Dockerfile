# Imagem base do Python
FROM python:3.11-slim

# Instala o uv (gestor de dependências)
RUN pip install uv

# Define o diretório de trabalho
WORKDIR /app

# Copia os arquivos de configuração do projeto
COPY pyproject.toml uv.lock ./

# Instala as dependências no ambiente do container
RUN uv sync --frozen

# Copia o restante do código
COPY . .

# Expõe a porta da aplicação
EXPOSE 8000

# Comando de inicialização
CMD ["./entrypoint.sh"]
