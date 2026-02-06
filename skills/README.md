# Project Chimera — Skills

Skills are **internal, deterministic capability packages** that the Chimera Agent executes. Per `specs/_meta.md`, Skills are stateless functions with no external side effects unless explicitly declared.

## Skill Inventory

| Skill | Purpose | Spec Reference |
|-------|---------|----------------|
| [fetch_trends](fetch_trends/README.md) | Fetch platform trends for content planning | US-001 |
| [download_video_metadata](download_video_metadata/README.md) | Download and store video metadata from platforms | US-002 |
| [generate_content_draft](generate_content_draft/README.md) | Generate content draft (script, captions, hooks) from brief | US-003 |

## Directory Structure

```
skills/
├── README.md                 # This file
├── fetch_trends/
│   ├── SKILL.md              # Agent instructions
│   └── README.md             # Input/Output contract
├── download_video_metadata/
│   ├── SKILL.md
│   └── README.md
└── generate_content_draft/
    ├── SKILL.md
    └── README.md
```

## Conventions

- **Input**: All skills accept `spec_id`, `agent_id`, and `params` for traceability
- **Output**: Structured JSON with `ok`, `data` (success) or `error`/`refusal` (failure)
- **Contracts**: Defined in each skill's README.md; source of truth is `specs/technical.md`
