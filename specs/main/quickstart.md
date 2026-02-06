# Project Chimera — Quickstart

**Branch**: `main` | **Date**: 2026-02-06

## Prerequisites

- Python 3.11+
- Docker (Postgres, Redis)
- MCP-compatible IDE (Cursor with Tenx MCP Sense)

## Setup

```bash
# Clone and enter repo
cd dy1

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Start infrastructure (when Docker Compose exists)
docker compose up -d postgres redis

# Run migrations (when Alembic exists)
alembic upgrade head

# Run contract tests
pytest tests/contract/ -v
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| DATABASE_URL | Postgres connection string | postgresql://localhost/chimera |
| REDIS_URL | Redis connection string | redis://localhost:6379 |
| OPENCLAW_GATEWAY_URL | OpenClaw Gateway WebSocket (optional) | — |
| OPENCLAW_GATEWAY_TOKEN | Gateway auth token (optional) | — |

## Key Paths

- **Specs**: `specs/_meta.md`, `specs/functional.md`, `specs/technical.md`
- **Skills**: `skills/`
- **Contracts**: `specs/main/contracts/`
- **Tests**: `tests/contract/`, `tests/integration/`, `tests/unit/`

## First Run

1. Ensure Postgres and Redis are running
2. Run `pytest tests/contract/` — all must pass before implementation
3. Implement Skills per specs/technical.md API contracts
