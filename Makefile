install:
	uv sync --no-cache

migrate:
	uv run python manage.py migrate contenttypes --noinput
	uv run python manage.py migrate auth --noinput
	uv run python manage.py migrate admin --noinput
	uv run python manage.py migrate --noinput

collectstatic:
	uv run python manage.py collectstatic --noinput

build:
	./build.sh

render-start:
	uv run gunicorn task_manager.wsgi