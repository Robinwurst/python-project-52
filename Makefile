install:
	uv sync --no-cache

migrate:
	uv run python manage.py migrate --noinput --fake-initial

collectstatic:
	uv run python manage.py collectstatic --noinput

build:
	./build.sh

render-start:
	uv run gunicorn task_manager.wsgi