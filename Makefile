install:
	uv sync --no-cache
	uv pip install -e .
	uv pip install django-bootstrap5
migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --noinput

build:
	./build.sh

render-start:
	curl -LsSf https://astral.sh/uv/install.sh  | sh && \
    uv run gunicorn task_manager.wsgi

test:
	uv run python3 manage.py test

format-app:
	uv run ruff check --fix task_manager