install:
	uv sync --no-cache

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --noinput

build:
	./build.sh

render-start:
	echo "Запускаем Gunicorn на порту ${PORT}"
	gunicorn task_manager.wsgi --bind 0.0.0.0:${PORT:-8000} --workers 4