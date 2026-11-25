FROM python:3.14

COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv sync --no-dev

COPY src/ src/
ENV PYTHONPATH="/app"
WORKDIR /app/data

ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 5001

CMD ["python", "/app/src/app.py"]