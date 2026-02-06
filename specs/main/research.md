# Project Chimera — Research (Phase 0)

**Branch**: `main` | **Date**: 2026-02-06

## Resolved Clarifications

### Language/Stack
- **Decision**: Python 3.11+ for core services; MCP for external integrations
- **Rationale**: SRS and 3-Day Challenge emphasize MCP, Python ecosystem has strong async and AI tooling
- **Alternatives**: Node.js (MCP native), Rust (performance) — Python chosen for rapid iteration and agent ecosystem

### Storage
- **Decision**: PostgreSQL (canonical) + TimescaleDB extension for metrics; Redis for queues/cache
- **Rationale**: Architecture strategy mandates SQL as truth; time-series for high-velocity engagement data
- **Alternatives**: MongoDB (rejected — no ACID for audit), ClickHouse (deferred to scale)

### Testing
- **Decision**: pytest with contract tests, integration tests, unit tests
- **Rationale**: Constitution requires Spec→Test→Code; pytest is standard for Python
- **Alternatives**: unittest (less ergonomic), Hypothesis (add for property-based later)

### Agent Pattern
- **Decision**: Hierarchical Swarm (Planner → Worker → Judge)
- **Rationale**: SRS and architecture strategy; scales horizontally, clear governance boundary
- **Alternatives**: Sequential chain (rejected — doesn't scale), Flat swarm (rejected — no governance)

### OpenClaw Integration
- **Decision**: Optional; WebSocket to Gateway, publish status via `chimera.status` event
- **Rationale**: Enables multi-agent discovery; not required for core functionality
- **Alternatives**: Polling (rejected — inefficient), Full Gateway node (future — start with status only)

## Dependencies & Best Practices

| Area | Practice |
|------|----------|
| MCP | Use MCP SDK for tool registration; emit trace events per Constitution |
| Postgres | Use async SQLAlchemy or asyncpg; migrations via Alembic |
| Redis | Use for task queues (e.g., arq, celery); short TTL for cache |
| API | JSON over HTTP/WebSocket; OpenAPI 3.0 for contracts |
