#!/bin/sh

set -e
exec poetry run alembic upgrade head
exec poetry run uvicorn fastapi_demo.asgi:app --reload