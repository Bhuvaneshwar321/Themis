# Architecture and Design Decisions (ADR)

This file tracks major design and architecture decisions for THEMIS.

## 2026-09-30: Project Restart
- **Decision:** Rebuild the project from scratch, abandoning the previous React/FastAPI codebase.
- **Reason:** The old codebase returned mock data, swallowed errors, used unnecessary heavy dependencies (torch, whisper), and lacked real retrieval/LLM integration. We are prioritizing a clean slate.

## 2026-09-30: Database Selection
- **Decision:** Use PostgreSQL 16 + pgvector as the sole database.
- **Reason:** Reduces architectural complexity by removing the need for a separate vector database (e.g., Qdrant) and cache (e.g., Redis) while natively supporting full-text search and embeddings.

## 2026-09-30: Embeddings Strategy
- **Decision:** Use BAAI `bge-m3` via `sentence-transformers` running locally.
- **Reason:** Provides strong multilingual support (crucial for English, Tamil, Hindi) without relying on expensive hosted APIs for every query.

## 2026-09-30: LLM Strategy
- **Decision:** Use Gemini API as the primary LLM, with a Groq-hosted Llama fallback, wrapped behind a common interface outputting JSON.
- **Reason:** Ensures high performance and availability without locking into a complex 3-vendor tiering system. JSON-schema output is required for the structured answer format.

## 2026-10-01: Tenancy Scenario Target State
- **Decision:** Tamil Nadu is chosen as the target state for the Illegal Eviction scenario.
- **Reason:** Tamil is one of the target languages for the application, making Tamil Nadu a logical starting point for state-specific laws.

## 2026-10-01: Local Development Configuration
- **Decision:** Use Vite proxy (`/api` -> `http://127.0.0.1:8000`) for local frontend-to-backend communication.
- **Reason:** Prevents CORS issues during local development without needing complex CORS configurations in FastAPI specifically for localhost ports.

## 2026-10-01: Postgres Image
- **Decision:** Use `pgvector/pgvector:pg16` for the database in `docker-compose.yml`.
- **Reason:** Provides PostgreSQL 16 bundled with the `pgvector` extension, meeting the project's vector search requirements directly out of the box without building a custom image.
