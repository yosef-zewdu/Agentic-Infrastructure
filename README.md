# Project Chimera — Agentic Infrastructure Challenge


## 1. What is Project Chimera?

Project Chimera is an **agentic infrastructure challenge**.

The goal is to design and govern a **robust engineering factory** capable of producing **Autonomous AI Influencers**—digital entities that can:
- perceive trends and signals,
- generate multimodal content,
- manage engagement,
- and (eventually) operate with economic agency,

This repository intentionally prioritizes:
- clarity of intent,
- strong contracts,
- safety and governance,
- and infrastructure discipline,

so that a **swarm of AI agents** can safely enter the codebase and build features with minimal human conflict.

---

## 2. Core Philosophy

### Spec‑Driven Development (SDD)

This project follows **Spec‑Driven Development**:

- **Specifications are the source of truth**
- No implementation code is written until specs are **ratified**
- Tests are written **before** implementations

---

## 3. Architecture Overview

### Agent Pattern

Project Chimera uses a **Hierarchical Swarm** architecture:

- **Planner** — decomposes goals into task DAGs
- **Worker** — executes atomic tasks (generation, research, actions)
- **Judge** — enforces policy, quality, and safety; commits state

Sequential chains may exist **inside** Workers, but **never** define system‑level orchestration.

### Integration Boundary

All external interactions go through **MCP (Model Context Protocol)** servers.

- No direct API calls from agents
- Tool usage is auditable, constrained, and reviewable

---

## 4. Safety & Governance Model

### Human‑in‑the‑Loop (HITL)

Humans are involved **only at explicit risk boundaries**, enforced by the Judge layer:

- High‑risk content publication
- Ambiguous or adversarial engagement
- Persona or long‑term memory mutation
- Agentic commerce above policy thresholds

This enables **management‑by‑exception**, not constant supervision.

---

## 5. Test‑Driven Development (TDD)

This repo intentionally contains **failing tests**.

Why?
- Tests define the *contract* the AI must satisfy
- They create an objective success criterion
- They prevent subjective “looks good to me” implementations

Current tests assert:
- Trend data structures match the API contract
- Skills modules expose correct interfaces

---

## 6. CI/CD & AI Governance

- GitHub Actions runs `make test` on every push and PR
- Automated review (e.g. CodeRabbit) is configured to:
  - check spec alignment
  - flag security issues
  - enforce architectural constraints

---


## Repository Structure

```
Agentic-Infrastructure/
├── .cursor/
│   ├── commands/
│   ├── rules/
│   └── mcp.json
│
├── .github/
│   ├── agents/
│   ├── prompts/
│   ├── workflows/
│   └── copilot-instructions.md
│
├── .specify/                   
├── .vscode/
│   ├── mcp.json
│   └── settings.json
│
├── ide-chat-history/
│
├── research/
│   ├── architecture_strategy.md
│   └── tooling_strategy.md
│
├── scripts/
│   └── spec_check.py
│
├── skills/
│   ├── download_video_metadata/
│   ├── fetch_trends/
│   └── generate_content_draft/
│
├── specs/
│   └── main/
│   ├── _meta.md
│   ├── functional.md
│   ├── openclaw_integration.md
│   └── technical.md
│
├── tests/
│   ├── test_skills_interface.py
│   └── test_trend_fetcher.py
│
├── .coderabbit.yaml
├── .dockerignore
├── .gitignore
├── Dockerfile
├── Makefile
├── README.md                  
└── requirements.txt

```

## Development Workflow

### Local Setup

```bash
make setup
```

### Run Tests (expected to fail initially)

```bash
make test
```
---

