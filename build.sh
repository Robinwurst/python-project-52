#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
poetry install

# Convert static asset files
poetry run python3 manage.py collectstatic --no-input

# Apply any outstanding database migrations
poetry run python3 manage.py migrate





##!/usr/bin/env bash
#
#curl -LsSf https://astral.sh/uv/install.sh | sh
#source $HOME/.local/bin/env
#export PYTHONPATH=/project/code
#cd /project/code
#uv run pytest
#
#make install && make collectstatic && make compilemessages && make migrate
#
