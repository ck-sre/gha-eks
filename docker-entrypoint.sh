#!/bin/sh

set -e

exec poetry run uvicorn fastapi_demo.asgi:app --reload