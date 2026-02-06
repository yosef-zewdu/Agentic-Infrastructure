# Project Chimera — Data Model (Phase 1)

**Branch**: `main` | **Date**: 2026-02-06  
**Source**: specs/technical.md

## Entity Summary

| Entity | Purpose |
|--------|---------|
| persona | Influencer identity, SOUL.md reference |
| campaign | Content campaign grouping |
| brief | Content brief (requirements, type) |
| video | Canonical video metadata (platform-agnostic) |
| draft | Generated content draft pre-publication |
| content | Published content with platform linkage |
| engagement_metric | Time-series metrics (views, likes, etc.) |
| review | Judge review outcome |
| trend_snapshot | Cached trend data |

## Relationships

- persona 1:N campaign
- campaign 1:N brief
- brief 1:N draft
- draft 1:1 content (after approval)
- content 1:N engagement_metric
- draft 1:N review
- video referenced by content (optional — for reposts/remixes)

## State Transitions

### Draft
`created` → `submitted` → `approved` | `rejected` | `escalated`

### Content
`ready_for_publish` → `publishing` → `published` | `failed`

### Campaign
`draft` → `active` → `paused` | `completed`

## Validation Rules

- `video.platform_id` + `video.platform` UNIQUE
- `draft.review_outcome` IN ('pending','approved','rejected','escalated')
- `content.publish_state` IN ('draft','ready','publishing','published','failed')
