---
name: english-docs-policy
description: Enforces the project language policy — all documentation is English-only regardless of conversation language. Use whenever creating, editing, or reviewing any Markdown file, spec, plan, checklist, or other project documentation in the Margan project.
---

# English-Only Documentation Policy

## The Rule

**All project documentation is written in English only**, no matter what language the conversation with the user is held in (the user typically communicates in Russian).

This applies to:
- All Markdown (`.md`) files — specs, use cases, reference materials, checklists, READMEs
- Plans, artifacts, and generated documents
- Comments in scripts and code
- Commit messages
- File and directory names (English, kebab/snake case)

## The Only Exception: Domain Terms & Glossary Content

Non-English text is allowed **only** where the term itself must be in another language:

- **Hebrew/Yiddish domain terms** in original script or transliteration where the term is the subject matter: *Vort* (ווארט), *Shtar Tna'im*, *Meurasim*, *Azmana*, *sheitel*, קייטרינג category names, etc. Give the English explanation alongside the term.
- **Glossary entries** and parameter catalogs that document multilingual terminology.
- **Verbatim source data**: vendor names, template texts (e.g., traditional invitation *Nusach* wording), quoted announcement formats — these stay in their original language because they *are* the content.

Rule of thumb: the surrounding prose, headings, tables, and explanations are always English; only the term or quoted artifact itself may be Hebrew/Yiddish/other.

## How to Apply

1. Before writing or editing any documentation file, confirm the content language is English — even if the user dictated the requirements in Russian.
2. When the user supplies content in Russian (decisions, models, descriptions), **translate it into English** for the document; reply to the user in Russian as usual.
3. If an existing file is found with non-English prose (outside the exceptions above), flag it and translate it to English.
4. Never mix languages within prose. A Hebrew term inside an English sentence is fine; a Russian sentence inside a spec is not.
