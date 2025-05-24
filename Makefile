install:
	uv sync --no-cache

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --noinput

build:
	./build.sh

render-start:
	source $HOME/.local/bin/env & uv run python gunicorn