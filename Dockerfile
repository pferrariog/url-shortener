FROM python:3.11-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN apt-get update && apt-get install -y libpq-dev gcc

RUN pip install poetry

COPY . .

RUN poetry install --without dev --no-interaction --no-ansi

EXPOSE 8000

RUN chmod +x /app/docker-entrypoint.sh

CMD ["./docker-entrypoint.sh"]
