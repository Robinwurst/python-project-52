lint:
	uv run flake8 task_manager

install:
	uv sync

dev:
	uv run python3 manage.py runserver

migrate:
	uv run python3 manage.py makemigrations
	uv run python3 manage.py migrate

build:
	./build.sh

start:
	uv run gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

test:
	uv run python3 manage.py test

testcov:
	uv run coverage run --source='.' manage.py test

makemessages:
	uv run django-admin makemessages --ignore="static" --ignore=".env"  -l ru

compilemessages:
	uv run django-admin compilemessages

ruff:
	ruff check --fix --select I