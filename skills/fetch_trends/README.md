# skill_fetch_trends

**Spec**: CHIMERA-FUNC-001 | **User Story**: US-001

Fetches current platform trends and topic signals for content planning.

## Input Contract

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `spec_id` | string | Yes | Spec identifier (e.g., CHIMERA-FUNC-001) |
| `agent_id` | string | No | Calling agent identifier |
| `agent_version` | string | No | Agent version |
| `params.platform` | enum | Yes | `tiktok` \| `youtube` \| `instagram` |
| `params.time_range_hours` | integer | No | Default: 24 |
| `params.limit` | integer | No | Max trends to return; default: 50 |

**Example**:
```json
{
  "spec_id": "CHIMERA-FUNC-001",
  "agent_id": "planner-001",
  "params": {
    "platform": "tiktok",
    "time_range_hours": 24,
    "limit": 50
  }
}
```

## Output Contract

### Success

| Field | Type | Description |
|-------|------|-------------|
| `ok` | boolean | `true` |
| `data.trends` | array | List of trend objects |
| `data.trends[].topic` | string | Topic/hashtag name |
| `data.trends[].volume` | integer | Search/mention volume |
| `data.trends[].trend_direction` | enum | `up` \| `down` \| `stable` |
| `data.trends[].source` | string | Data source identifier |
| `data.trends[].fetched_at` | string | ISO8601 timestamp |
| `data.platform` | string | Echo of requested platform |
| `data.time_range_hours` | integer | Echo of requested range |

### Error

| Field | Type | Description |
|-------|------|-------------|
| `ok` | boolean | `false` |
| `error.error_code` | string | e.g., `PLATFORM_UNAVAILABLE` |
| `error.message` | string | Human-readable message |
| `error.retry_after_seconds` | integer | Optional; when to retry |
