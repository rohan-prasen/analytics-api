# Build an Analytics API using FastAPI + Time-series Postgres

Own your data pipeline!

Start by build an Analytical API service using Python, FastAPI, and Time-series Postgres with TimescaleDB

## Docker

- `docker  build -t analytics-api -f Dockerfile.web .`
- `docker run analytics-api`

becomes

- `docker compose up --watch`
- `docker compose down` or `docker compose down -v` (to remove volumes)
- `docker compose run app /bin/bash` (to get a bash shell in the app container)
