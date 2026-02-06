---
name: download-video-metadata
description: Downloads and stores video metadata from YouTube, TikTok, or Instagram. Use when analyzing content, avoiding duplicates, or building a video metadata catalog.
---

# Download Video Metadata

## Purpose

Fetches metadata for a video URL and persists it in the canonical store. Supports YouTube, TikTok, Instagram.

## When to Use

- Before reposting or remixing content
- Content performance analysis
- Duplicate detection
- Trend/competitor research

## Input

See [README.md](README.md) for full contract. Required: `spec_id`, `params.url`.

## Output

Video metadata object or structured error. Duplicate URLs return existing record.

## Implementation Notes

- Use platform-specific MCP Tools or adapters for API calls
- Persist to Postgres `video` table per `specs/technical.md` ERD
- Emit trace event for external API calls
- Idempotent: same URL → same record
