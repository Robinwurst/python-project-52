install:
	uv sync --no-cache

migrate:
	uv run python3 manage.py makemigrations
	uv run python3 manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --noinput

build:
	./build.sh

render-start:
	curl -LsSf https://astral.sh/uv/install.sh | sh && uv run gunicorn task_manager.wsgi

test:
	uv run python3 manage.py test

compilemessages:
	uv run django-admin compilemessages

makemessages:
	uv run django-admin makemessages --ignore="static" --ignore=".env"  -l ru