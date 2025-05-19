install:
	uv sync --no-cache

migrate:
	echo "Resetting migrations..."
	python manage.py migrate --fake
	python manage.py migrate --fake-initial

collectstatic:
	uv run python manage.py collectstatic --noinput

build:
	./build.sh

render-start:
	uv run gunicorn task_manager.wsgi