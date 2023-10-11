FROM python:3.11-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

RUN apt update && apt install -y libpq-dev

RUN pip install poetry

COPY . .

RUN poetry install --without dev --no-interaction --no-ansi

EXPOSE 8000

RUN chmod +x /app/docker-entrypoint.sh

CMD ["./docker-entrypoint.sh"]
