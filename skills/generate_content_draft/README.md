# skill_generate_content_draft

**Spec**: CHIMERA-FUNC-001 | **User Story**: US-003

Generates a content draft (script, captions, hooks) from a brief and persona.

## Input Contract

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `spec_id` | string | Yes | Spec identifier |
| `agent_id` | string | No | Calling agent identifier |
| `params.brief_id` | uuid | Yes | Content brief ID |
| `params.persona_id` | uuid | Yes | Persona (SOUL.md) reference |
| `params.content_type` | enum | No | `short_form` \| `long_form` \| `story`; default from brief |

**Example**:
```json
{
  "spec_id": "CHIMERA-FUNC-001",
  "agent_id": "worker-001",
  "params": {
    "brief_id": "550e8400-e29b-41d4-a716-446655440000",
    "persona_id": "550e8400-e29b-41d4-a716-446655440001",
    "content_type": "short_form"
  }
}
```

## Output Contract

### Success

| Field | Type | Description |
|-------|------|-------------|
| `ok` | boolean | `true` |
| `data.draft_id` | uuid | Draft record ID |
| `data.script` | string | Full script text |
| `data.captions` | array | Caption variants (platform-specific) |
| `data.hooks` | array | Hook/opening line variants |
| `data.model_version` | string | Model used for generation |
| `data.spec_id` | string | Echo of spec_id |
| `data.created_at` | string | ISO8601 timestamp |

### Refusal (Safety Filter)

| Field | Type | Description |
|-------|------|-------------|
| `ok` | boolean | `false` |
| `refusal.refusal_code` | string | e.g., `SAFETY_FILTER` |
| `refusal.reason` | string | Explanation |
| `refusal.required_action` | string | What must be supplied |
| `refusal.escalation_path` | string | Governance ticket template |

## Notes

- Draft is submitted to Judge for approval before publication
- Safety filters may refuse generation; do not auto-retry
