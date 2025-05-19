install:
	uv sync --no-cache

migrate:
	uv run python manage.py migrate users --fake
	uv run python manage.py migrate admin --fake
	uv run python manage.py migrate --run-syncdb
	uv run python manage.py migrate --fake-initial

collectstatic:
	uv run python manage.py collectstatic --noinput

build:
	./build.sh

render-start:
	uv run gunicorn task_manager.wsgi