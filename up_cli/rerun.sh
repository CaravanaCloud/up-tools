rm -rf "/workspace/.pyenv_mirror/poetry/virtualenvs/"up*
poetry cache clear . --all --no-interaction
poetry install
poetry run up vars: USER UALA
