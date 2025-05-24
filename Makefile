install:
	uv sync --no-cache

migrate:
	uv run python manage.py migrate

collectstatic:
	uv run python manage.py collectstatic --noinput

build:
	./build.sh

render-start:
	curl -LsSf https://astral.sh/uv/install.sh | sh && uv run gunicorn task_manager.wsgi