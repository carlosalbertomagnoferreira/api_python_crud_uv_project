FROM ghcr.io/astral-sh/uv:python3.11-alpine AS builder

WORKDIR /app

COPY . .

RUN uv sync --frozen

FROM python:3.11-alpine3.22

RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY --from=builder --chown=appuser:appgroup /app /app

ENV PATH="/app/.venv/bin:$PATH"

USER appuser

WORKDIR /app

EXPOSE 8000

CMD ["./entrypoint.sh"]