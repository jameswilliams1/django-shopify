#!/bin/bash

set -eu

ROOT_DIR="$(cd "$(dirname "$(dirname "${BASH_SOURCE[0]}")")" && pwd)"

python "$ROOT_DIR/manage.py" collectstatic --noinput
python "$ROOT_DIR/manage.py" migrate
gunicorn config.wsgi --bind 0.0.0.0:5000 --chdir="$ROOT_DIR"
