# Project Chimera — Technical Specification

**Spec-ID**: CHIMERA-TECH-001  
**Spec-Status**: DRAFT  
**Ratified-By**: TODO  
**Ratified-On**: TODO  
**Autonomy-Approval**: false  
**Allowed-Tools**: []  
**Rate-Limits**: {}  
**Safety-Constraints**: {}

---

## 1. API Contracts (JSON Inputs/Outputs)

All agent-facing APIs use JSON. Each contract includes `spec_id` and `agent_id` for traceability.

---

### 1.1 Fetch Trends

**Endpoint**: `skills/fetch_trends` (internal Skill)  
**Method**: N/A (Skill invocation)

**Input**:
```json
{
  "spec_id": "CHIMERA-FUNC-001",
  "agent_id": "string",
  "agent_version": "string",
  "params": {
    "platform": "tiktok | youtube | instagram",
    "time_range_hours": 24,
    "limit": 50
  }
}
```

**Output (success)**:
```json
{
  "ok": true,
  "data": {
    "trends": [
      {
        "topic": "string",
        "volume": 1000,
        "trend_direction": "up | down | stable",
        "source": "string",
        "fetched_at": "2026-02-06T12:00:00Z"
      }
    ],
    "platform": "tiktok",
    "time_range_hours": 24
  }
}
```

**Output (error)**:
```json
{
  "ok": false,
  "error": {
    "error_code": "PLATFORM_UNAVAILABLE",
    "message": "string",
    "retry_after_seconds": 60
  }
}
```

---

### 1.2 Download Video Metadata

**Endpoint**: `skills/download_video_metadata` (Skill → MCP Tool)

**Input**:
```json
{
  "spec_id": "CHIMERA-FUNC-001",
  "agent_id": "string",
  "params": {
    "url": "https://...",
    "platform": "tiktok | youtube | instagram"
  }
}
```

**Output (success)**:
```json
{
  "ok": true,
  "data": {
    "video_id": "uuid",
    "platform_id": "string",
    "platform": "tiktok",
    "title": "string",
    "description": "string",
    "duration_seconds": 60,
    "creator_id": "string",
    "creator_handle": "string",
    "published_at": "2026-02-06T12:00:00Z",
    "url": "https://...",
    "thumbnail_url": "https://...",
    "created_at": "2026-02-06T12:05:00Z"
  }
}
```

**Output (error)**:
```json
{
  "ok": false,
  "error": {
    "error_code": "INVALID_URL | PRIVATE_VIDEO | RATE_LIMITED",
    "message": "string"
  }
}
```

---

### 1.3 Generate Content Draft

**Input**:
```json
{
  "spec_id": "CHIMERA-FUNC-001",
  "agent_id": "string",
  "params": {
    "brief_id": "uuid",
    "persona_id": "uuid",
    "content_type": "short_form | long_form | story"
  }
}
```

**Output (success)**:
```json
{
  "ok": true,
  "data": {
    "draft_id": "uuid",
    "script": "string",
    "captions": ["string"],
    "hooks": ["string"],
    "model_version": "string",
    "spec_id": "CHIMERA-FUNC-001",
    "created_at": "2026-02-06T12:00:00Z"
  }
}
```

**Output (refusal)**:
```json
{
  "ok": false,
  "refusal": {
    "refusal_code": "SAFETY_FILTER",
    "reason": "string",
    "required_action": "string",
    "escalation_path": "string"
  }
}
```

---

### 1.4 Submit for Judge Review

**Input**:
```json
{
  "spec_id": "CHIMERA-FUNC-001",
  "agent_id": "string",
  "params": {
    "draft_id": "uuid",
    "risk_level": "low | medium | high"
  }
}
```

**Output**:
```json
{
  "ok": true,
  "data": {
    "review_id": "uuid",
    "outcome": "approved | rejected | escalated_to_hitl",
    "reason": "string",
    "feedback": "string",
    "hitl_ticket_id": "uuid | null"
  }
}
```

---

### 1.5 Publish Content

**Input**:
```json
{
  "spec_id": "CHIMERA-FUNC-001",
  "agent_id": "string",
  "params": {
    "draft_id": "uuid",
    "platform": "tiktok | youtube | instagram",
    "idempotency_key": "uuid"
  }
}
```

**Output (success)**:
```json
{
  "ok": true,
  "data": {
    "content_id": "uuid",
    "platform_url": "https://...",
    "publish_state": "published",
    "published_at": "2026-02-06T12:00:00Z"
  }
}
```

**Output (retry)**:
```json
{
  "ok": false,
  "error": {
    "error_code": "RATE_LIMITED",
    "retry_after_seconds": 60,
    "message": "string"
  }
}
```

---

### 1.6 Fetch Engagement Metrics

**Input**:
```json
{
  "spec_id": "CHIMERA-FUNC-001",
  "agent_id": "string",
  "params": {
    "content_id": "uuid",
    "platform": "tiktok | youtube | instagram"
  }
}
```

**Output (success)**:
```json
{
  "ok": true,
  "data": {
    "content_id": "uuid",
    "views": 1000,
    "likes": 50,
    "comments": 10,
    "watch_time_seconds": 45000,
    "fetched_at": "2026-02-06T12:00:00Z",
    "status": "indexed | pending"
  }
}
```

---

## 2. Database Schema (ERD)

### 2.1 Entity-Relationship Diagram

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│    persona      │       │     campaign    │       │     brief       │
├─────────────────┤       ├─────────────────┤       ├─────────────────┤
│ id (PK)         │───┐   │ id (PK)         │   ┌───│ id (PK)         │
│ name            │   │   │ persona_id (FK) │   │   │ campaign_id (FK)│
│ soul_md_ref     │   └──▶│ status          │   └──▶│ content_type    │
│ created_at      │       │ created_at      │       │ requirements    │
│ updated_at      │       │ updated_at      │       │ created_at      │
└─────────────────┘       └─────────────────┘       └─────────────────┘
         │                            │                         │
         │                            │                         │
         ▼                            ▼                         ▼
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│     video       │       │     content     │       │     draft        │
├─────────────────┤       ├─────────────────┤       ├─────────────────┤
│ id (PK)         │◀──────│ id (PK)         │◀──────│ id (PK)         │
│ platform_id (UQ)│       │ draft_id (FK)   │       │ brief_id (FK)    │
│ platform        │       │ persona_id (FK) │       │ persona_id (FK)  │
│ title           │       │ platform        │       │ script           │
│ description     │       │ platform_url    │       │ captions (JSONB) │
│ duration_secs   │       │ publish_state   │       │ hooks (JSONB)    │
│ creator_id      │       │ published_at    │       │ model_version    │
│ creator_handle  │       │ created_at      │       │ review_outcome   │
│ published_at    │       │ updated_at      │       │ created_at      │
│ url             │       └─────────────────┘       │ updated_at      │
│ thumbnail_url   │                 │               └─────────────────┘
│ created_at      │                 │
└─────────────────┘                 │
                                    ▼
                          ┌─────────────────┐
                          │ engagement_metric│
                          ├─────────────────┤
                          │ id (PK)         │
                          │ content_id (FK) │
                          │ views           │
                          │ likes           │
                          │ comments        │
                          │ watch_time_secs │
                          │ fetched_at      │
                          └─────────────────┘

┌─────────────────┐       ┌─────────────────┐
│  review         │       │  trend_snapshot  │
├─────────────────┤       ├─────────────────┤
│ id (PK)         │       │ id (PK)         │
│ draft_id (FK)   │       │ platform        │
│ outcome         │       │ topic           │
│ risk_level      │       │ volume          │
│ hitl_ticket_id  │       │ trend_direction │
│ created_at      │       │ fetched_at      │
└─────────────────┘       └─────────────────┘
```

---

### 2.2 Table Definitions (Postgres)

#### `persona`
| Column      | Type        | Constraints |
|-------------|-------------|-------------|
| id          | UUID        | PK, DEFAULT gen_random_uuid() |
| name        | VARCHAR(255)| NOT NULL    |
| soul_md_ref | TEXT        |             |
| created_at  | TIMESTAMPTZ | NOT NULL    |
| updated_at  | TIMESTAMPTZ | NOT NULL    |

#### `campaign`
| Column      | Type        | Constraints |
|-------------|-------------|-------------|
| id          | UUID        | PK          |
| persona_id  | UUID        | FK → persona|
| status      | VARCHAR(50) | NOT NULL   |
| created_at  | TIMESTAMPTZ | NOT NULL    |
| updated_at  | TIMESTAMPTZ | NOT NULL    |

#### `brief`
| Column        | Type        | Constraints |
|---------------|-------------|-------------|
| id            | UUID        | PK          |
| campaign_id   | UUID        | FK → campaign|
| content_type  | VARCHAR(50) | NOT NULL    |
| requirements  | JSONB       |             |
| created_at    | TIMESTAMPTZ | NOT NULL    |

#### `video` (canonical video metadata)
| Column         | Type        | Constraints |
|----------------|-------------|-------------|
| id             | UUID        | PK          |
| platform_id    | VARCHAR(255)| UNIQUE      |
| platform       | VARCHAR(50) | NOT NULL    |
| title          | TEXT        |             |
| description    | TEXT        |             |
| duration_secs  | INT         |             |
| creator_id     | VARCHAR(255)|             |
| creator_handle | VARCHAR(255)|             |
| published_at   | TIMESTAMPTZ |             |
| url            | TEXT        |             |
| thumbnail_url  | TEXT        |             |
| created_at     | TIMESTAMPTZ | NOT NULL    |

#### `draft`
| Column        | Type        | Constraints |
|---------------|-------------|-------------|
| id            | UUID        | PK          |
| brief_id      | UUID        | FK → brief  |
| persona_id    | UUID        | FK → persona|
| script        | TEXT        |             |
| captions      | JSONB       |             |
| hooks         | JSONB       |             |
| model_version | VARCHAR(100)|             |
| review_outcome| VARCHAR(50) |             |
| created_at    | TIMESTAMPTZ | NOT NULL    |
| updated_at    | TIMESTAMPTZ | NOT NULL    |

#### `content`
| Column        | Type        | Constraints |
|---------------|-------------|-------------|
| id            | UUID        | PK          |
| draft_id      | UUID        | FK → draft  |
| persona_id    | UUID        | FK → persona|
| platform      | VARCHAR(50) | NOT NULL    |
| platform_url  | TEXT        |             |
| publish_state | VARCHAR(50) | NOT NULL    |
| published_at  | TIMESTAMPTZ |             |
| created_at    | TIMESTAMPTZ | NOT NULL    |
| updated_at    | TIMESTAMPTZ | NOT NULL    |

#### `engagement_metric` (time-series; consider hypertable for scale)
| Column          | Type        | Constraints |
|-----------------|-------------|-------------|
| id              | UUID        | PK          |
| content_id      | UUID        | FK → content|
| views           | BIGINT      |             |
| likes           | BIGINT      |             |
| comments        | BIGINT      |             |
| watch_time_secs | BIGINT      |             |
| fetched_at      | TIMESTAMPTZ | NOT NULL    |

#### `review`
| Column         | Type        | Constraints |
|----------------|-------------|-------------|
| id             | UUID        | PK          |
| draft_id       | UUID        | FK → draft  |
| outcome        | VARCHAR(50) | NOT NULL    |
| risk_level     | VARCHAR(20) |             |
| hitl_ticket_id | UUID        |             |
| created_at     | TIMESTAMPTZ | NOT NULL    |

#### `trend_snapshot`
| Column          | Type        | Constraints |
|-----------------|-------------|-------------|
| id              | UUID        | PK          |
| platform        | VARCHAR(50) | NOT NULL    |
| topic           | VARCHAR(255)| NOT NULL    |
| volume          | INT         |             |
| trend_direction | VARCHAR(20) |             |
| fetched_at      | TIMESTAMPTZ | NOT NULL    |

---

## 3. Time-Series Storage (Metrics)

High-velocity engagement metrics SHOULD use **TimescaleDB** (Postgres extension) or a dedicated OLAP store:

- `engagement_metric` → hypertable on `fetched_at`
- Retention policy: 90 days hot, 1 year cold (configurable)
- Aggregation views for dashboards

---

## 4. Trace Storage

Per Constitution Section 6: All MCP/Tool calls MUST emit structured trace events. Store in append-only log:

| Field        | Type        |
|--------------|-------------|
| timestamp    | TIMESTAMPTZ |
| actor_id     | VARCHAR     |
| spec_id      | VARCHAR     |
| call_id      | UUID        |
| input_hash   | VARCHAR(64) |
| endpoint     | TEXT        |
| response_hash| VARCHAR(64) |
| outcome      | VARCHAR(20) |
