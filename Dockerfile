# Imagem base do Python
FROM python:3.11-slim

# Atualiza pacotes do sistema para corrigir vulnerabilidades
RUN apt-get update && apt-get upgrade -y && apt-get clean

# Instala uv (gestor de dependências)
RUN pip install uv

# Criar um grupo e um usuário não-root com IDs específicos para consistência em diferentes ambientes
RUN groupadd appgroup && useradd -g appgroup -s /bin/sh -m appuser

# Definir o diretório de trabalho e garantir que o novo usuário tenha as permissões corretas
WORKDIR /app
RUN chown -R appuser:appgroup /app

# Mudar para o usuário não-root antes de copiar arquivos e executar a aplicação
USER appuser

# Copiar os arquivos da aplicação
COPY --chown=appuser:appgroup . /app

# Instala dependências do pyproject.toml
RUN uv sync --frozen

# Expõe porta da API
EXPOSE 8000

# Comando padrão: entrypoint
CMD ["./entrypoint.sh"]
