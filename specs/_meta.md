# Project Chimera — Meta Specification

**Spec-ID**: CHIMERA-META-001  
**Spec-Status**: DRAFT  
**Ratified-By**: TODO  
**Ratified-On**: TODO  
**Autonomy-Approval**: false  
**Allowed-Tools**: []  
**Rate-Limits**: {}  
**Safety-Constraints**: {}

---

## 1. Vision

Project Chimera is an **Autonomous Influencer Network** — a factory for persistent, goal-directed AI agents capable of:

- **Perception** — ingesting trends, platform signals, and audience feedback
- **Reasoning** — planning content, engagement, and campaigns
- **Creative Expression** — generating and publishing media
- **Economic Agency** — transacting via non-custodial wallets (Agentic Commerce)

The system is **not** a one-off demo. It is **infrastructure** that scales to many agents, many concurrent tasks, and multiple platforms.

---

## 2. Architectural Principles

| Principle | Constraint |
|-----------|------------|
| **Spec-Driven Development (SDD)** | No implementation without a RATIFIED spec. Specs own intent, contracts, schemas, and safety. |
| **Hierarchical Swarm** | Planner → Worker → Judge. No sequential chains at system level. |
| **MCP as Integration Boundary** | All external I/O (platforms, tools, databases) via Model Context Protocol. |
| **Judge-Centric Governance** | Validation, policy, and state commits at the Judge layer. HITL at defined gates only. |
| **SQL as Truth** | Postgres for canonical metadata and audit. Time-series/OLAP for high-velocity metrics. |

---

## 3. Agent Roles

| Role | Responsibility |
|------|----------------|
| **Planner** | Decomposes goals into task DAGs. No side effects. |
| **Worker** | Executes atomic tasks (generate, research, post, fetch). May use Skills and MCP Tools. |
| **Judge** | Validates outputs, enforces policy, commits state. Mandatory HITL gates for high-risk actions. |

---

## 4. Human-in-the-Loop (HITL) Gates

Human approval is **required** at the Judge layer for:

1. **Content Publication** — politics, health, finance, legal, brand-sensitive
2. **Engagement/Reply** — low-confidence intent, adversarial interactions, external links
3. **Persona/Memory Mutation** — SOUL.md changes, identity-impacting memory writes
4. **Agentic Commerce** — transactions above policy thresholds, new counterparties

---

## 5. Skills vs Tools

| Type | Definition | Side Effects |
|------|------------|--------------|
| **Skill** | Internal, deterministic capability (stateless function) | None unless declared |
| **Tool / MCP Server** | External, side-effectful capability (I/O, network, DB) | Yes — requires spec reference |

Every Tool call MUST include: `spec_id`, `call_purpose`, `call_authorization`.

---

## 6. Constraints

- **Scale**: Many agents, many concurrent tasks, multi-platform
- **Governance**: Full audit trail, tamper-evident logs, 90-day trace retention
- **Extensibility**: New platforms, models, and tools without redesign
- **No monolithic chains**: Sequential flows MAY exist inside a Worker only

---

## 7. Spec Hierarchy

```
specs/
├── _meta.md              ← This file (vision, constraints)
├── functional.md         ← Agent user stories
├── technical.md          ← API contracts, database schema
└── openclaw_integration.md  ← Optional: OpenClaw Availability/Status
```

---

## 8. Compliance

- All specs MUST include machine-interpretable header fields (Section 12 of Constitution).
- Implementation commits MUST reference `Spec:` and `Test:` in commit body.
- CI MUST validate spec references and SDD compliance.
