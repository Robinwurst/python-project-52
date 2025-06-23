#!/usr/bin/env bash

curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env
export PYTHONPATH=/project/code
cd /project/code


make install && make collectstatic && make compilemessages && make migrate
