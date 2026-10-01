---
name: rag-ingest
description: Ingests official legal source text into the pgvector legal_chunks table.
---
# Skill: RAG Ingestion

## Purpose
Parses official legal documents (India Code, Gazette) and inserts them into the `legal_chunks` table.

## Steps
1. **Download Raw Data:** Ensure official PDFs/text are in `data/raw/` and logged in `data/sources.json` (URL + retrieval date).
2. **Parse Sections:** Write/use a section-level parser. 
   - Rule: One chunk per section. Provisos/explanations stay with their section.
   - Rule: Split very long sections using `part_index`.
3. **Generate Embeddings:** Embed the parsed text using the `bge-m3` model.
4. **Insert to DB:** Insert chunks into PostgreSQL with full-text search (TSV) and pgvector fields.

## Inputs
- Files in `data/raw/`.
- Schema: `id`, `act_name`, `act_year`, `chapter`, `section_number`, `section_title`, `part_index`, `text`, `language`, `source_url`, `retrieved_on`, `amended_through`, `status`, `embedding`, `tsv`.

## Outputs
- Populated `legal_chunks` table.
- Idempotent script: `python -m ingest.run`.

## Checks
- Chunk counts match the official act's section count.
- No empty text or duplicate IDs.
