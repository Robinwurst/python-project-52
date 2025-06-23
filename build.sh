#!/usr/bin/env bash
# скачиваем uv
curl -LsSf https://astral.sh/uv/install.sh | sh
source $HOME/.local/bin/env

# здесь добавьте все необходимые команды для установки вашего проекта
# команду установки зависимостей, сборки статики, применения миграций и другие
make install && make collectstatic && make migrate


##!/usr/bin/env bash
#
#curl -LsSf https://astral.sh/uv/install.sh | sh
#source $HOME/.local/bin/env
#export PYTHONPATH=/project/code
#cd /project/code
#uv run pytest
#
#make install && make collectstatic && make compilemessages && make migrate
