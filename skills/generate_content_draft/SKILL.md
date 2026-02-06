---
name: generate-content-draft
description: Generates content drafts (script, captions, hooks) from a brief and persona. Use when creating content for publication, following a content brief, or when the Worker needs to produce draft material for Judge review.
---

# Generate Content Draft

## Purpose

Produces a content draft from a brief and persona. Output goes to Judge for policy/quality validation before publication.

## When to Use

- Content creation workflow
- Campaign execution
- After brief approval

## Input

See [README.md](README.md) for full contract. Required: `spec_id`, `params.brief_id`, `params.persona_id`.

## Output

Draft with script, captions, hooks, and provenance. Or structured refusal if safety filters trigger.

## Implementation Notes

- Load brief requirements and persona (SOUL.md) before generation
- Include `model_version` and `spec_id` for traceability
- On safety refusal: return refusal object; do not retry
- Persist draft to `draft` table per `specs/technical.md`
