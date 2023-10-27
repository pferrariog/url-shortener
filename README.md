# URL Shortener App

I don't like big URLs, so I made a way to shorten them, but not just for me.

## Usage

Instead of just an API, a webpage was created too. Just get to [URL Shortener Homepage](urlshortener.pedrohferrari.com) and try it yourself!

## How to Run

- Pure python
  - Create venv and install dependencies

        poetry shell && poetry install --without dev

  - Start app with uvicorn

        uvicorn url_shortener.app:app

- Docker
  - Run app with Docker Compose

        docker compose up --build

## Dependencies

- Python 3.11+
- Poetry 2.0+
- Docker (Optional)
