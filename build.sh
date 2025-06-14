#!/usr/bin/env bash

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
export PYTHONPATH=/project/code
cd /project/code
uv run pytest

make install && make collectstatic && make migrate

