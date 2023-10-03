#!/bin/bash

alembic upgrade head

# ls

# gunicorn src.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload