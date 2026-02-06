# skill_download_video_metadata

**Spec**: CHIMERA-FUNC-001 | **User Story**: US-002

Downloads and stores video metadata from supported platforms (YouTube, TikTok, Instagram).

## Input Contract

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `spec_id` | string | Yes | Spec identifier |
| `agent_id` | string | No | Calling agent identifier |
| `params.url` | string | Yes | Video URL (must be valid platform URL) |
| `params.platform` | enum | No | `tiktok` \| `youtube` \| `instagram`; can be inferred from URL |

**Example**:
```json
{
  "spec_id": "CHIMERA-FUNC-001",
  "agent_id": "worker-001",
  "params": {
    "url": "https://www.youtube.com/watch?v=...",
    "platform": "youtube"
  }
}
```

## Output Contract

### Success

| Field | Type | Description |
|-------|------|-------------|
| `ok` | boolean | `true` |
| `data.video_id` | uuid | Internal canonical ID |
| `data.platform_id` | string | Platform-native ID |
| `data.platform` | string | Platform name |
| `data.title` | string | Video title |
| `data.description` | string | Video description |
| `data.duration_seconds` | integer | Duration in seconds |
| `data.creator_id` | string | Creator/platform ID |
| `data.creator_handle` | string | Creator handle/username |
| `data.published_at` | string | ISO8601 publish timestamp |
| `data.url` | string | Canonical URL |
| `data.thumbnail_url` | string | Thumbnail URL |
| `data.created_at` | string | ISO8601 when stored |

### Error

| Field | Type | Description |
|-------|------|-------------|
| `ok` | boolean | `false` |
| `error.error_code` | enum | `INVALID_URL` \| `PRIVATE_VIDEO` \| `RATE_LIMITED` |
| `error.message` | string | Human-readable message |

## Idempotency

Duplicate URL returns existing record; no duplicate insert.
