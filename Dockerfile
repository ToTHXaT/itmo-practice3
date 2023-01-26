FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY pyproject.toml poetry.lock ./
RUN pip install poetry --no-cache-dir && poetry config virtualenvs.create false && poetry install --without dev

COPY src/* graph.csv terms.csv graph.html terms.html /app/