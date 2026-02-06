---
name: fetch-trends
description: Fetches platform trends (TikTok, YouTube, Instagram) for content planning. Use when the Planner or Worker needs trend data to inform content strategy, campaign decisions, or topic selection.
---

# Fetch Trends

## Purpose

Returns current trending topics and volume signals from a configured platform. Read-only; no side effects.

## When to Use

- Content planning and brief creation
- Campaign topic selection
- Competitive analysis inputs

## Input

See [README.md](README.md) for full contract. Required: `spec_id`, `params.platform`.

## Output

Structured trend list or error. Always include `spec_id` in response metadata.

## Implementation Notes

- Platform adapters (MCP Tools) may be used for actual API calls
- Cache results per platform/time_range to avoid rate limits
- Emit trace event per Constitution Section 6 when invoking external APIs
