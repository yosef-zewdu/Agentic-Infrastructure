# Implementation Plan: Project Chimera Blueprint

**Branch**: `main` | **Date**: 2026-02-06 | **Spec**: specs/_meta.md, specs/functional.md, specs/technical.md

**Input**: Full project blueprint per speckit.plan workflow

## Summary

Project Chimera is an Autonomous Influencer Network — infrastructure for persistent, goal-directed AI agents. This plan establishes the spec-driven blueprint: vision (_meta), agent user stories (functional), API contracts and database schema (technical), and optional OpenClaw integration.

## Technical Context

**Language/Version**: Python 3.11+  
**Primary Dependencies**: FastAPI (or equivalent), MCP SDK, asyncpg/SQLAlchemy, Redis  
**Storage**: PostgreSQL (canonical), TimescaleDB (metrics), Redis (queues/cache)  
**Testing**: pytest (contract, integration, unit)  
**Target Platform**: Linux server, Docker  
**Project Type**: Backend services + Skills + MCP Tools  
**Performance Goals**: 100+ concurrent tasks, &lt;500ms p95 for read operations  
**Constraints**: SDD compliance, 90-day trace retention, HITL at Judge gates  
**Scale/Scope**: Multi-agent, multi-platform, 10k+ videos metadata

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status |
|-----------|--------|
| Spec Precedence | ✓ specs/_meta, functional, technical, openclaw define intent |
| Spec Status | ✓ All specs include Spec-Status (DRAFT) |
| Implementation Gate | ✓ No code without Approved spec reference |
| Skills vs Tools | ✓ Documented in _meta; Tool calls require spec_id |
| MCP Observability | ✓ Trace events defined in technical.md |
| Git Hygiene | ✓ Commit format with Spec: and Test: required |

## Project Structure

### Documentation (this feature)

```text
specs/
├── _meta.md              # Vision, constraints (required)
├── functional.md         # Agent user stories (required)
├── technical.md          # API contracts, ERD (required)
├── openclaw_integration.md  # Optional OpenClaw
└── main/
    ├── plan.md           # This file
    ├── research.md       # Phase 0 output
    ├── data-model.md     # Phase 1 output
    ├── quickstart.md     # Phase 1 output
    └── contracts/        # Phase 1 output (OpenAPI)
```

### Source Code (repository root)

```text
src/
├── models/           # Domain entities
├── services/         # Planner, Worker, Judge logic
├── skills/           # Internal Skills (fetch_trends, etc.)
├── mcp/              # MCP tool adapters
└── api/              # HTTP/WebSocket entrypoints

tests/
├── contract/         # API contract tests
├── integration/      # End-to-end flows
└── unit/             # Unit tests

skills/               # Skill implementations (repo root)
```

**Structure Decision**: Single backend project; Skills at repo root per 3-Day Challenge; MCP as integration boundary.

## Generated Artifacts

| Artifact | Path |
|----------|------|
| Research | specs/main/research.md |
| Data Model | specs/main/data-model.md |
| Quickstart | specs/main/quickstart.md |
| Contracts | specs/main/contracts/agent-api.openapi.yaml |
| Meta Spec | specs/_meta.md |
| Functional Spec | specs/functional.md |
| Technical Spec | specs/technical.md |
| OpenClaw Spec | specs/openclaw_integration.md |

## Complexity Tracking

No constitution violations requiring justification.
