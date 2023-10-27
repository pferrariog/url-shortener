FROM python:3.11-slim

WORKDIR /app

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y libpq-dev gcc

RUN pip install poetry

COPY . .

RUN poetry install --without dev --no-interaction --no-ansi

EXPOSE 8000

RUN chmod +x /app/docker-entrypoint.sh

CMD ["./docker-entrypoint.sh"]
