install:
	uv sync --no-cache

migrate:
	uv run python3 manage.py migrate

collectstatic:
	uv run python3 manage.py collectstatic --noinput

build:
	./build.sh

render-start:
	source $HOME/.local/bin/env & uv run gunicorn