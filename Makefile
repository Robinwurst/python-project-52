install:
	uv sync

migrate:
	uv run python manage.py migrate --fake-initial

collectstatic:
	uv run python manage.py collectstatic --noinput

build:
	./build.sh

render-start:
	uv run gunicorn task_manager.wsgi