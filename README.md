# THEMIS - Justice in Your Language

THEMIS is an open-source, multilingual legal-information assistant for people in India. It helps users understand their rights and immediate next steps during stressful legal situations (e.g., a police stop, illegal eviction, unpaid wages). It uses citation-verified retrieval to ensure all information is grounded in official law and actively refuses to answer out-of-scope questions.

*Work in progress.*

## Quick Start

1. **Start the database:**
   ```bash
   docker compose up -d db
   ```

2. **Setup and run backend & frontend:**
   ```bash
   make setup
   make dev-backend
   ```
   In a new terminal:
   ```bash
   make dev-frontend
   ```
   
   The backend will be available at `http://localhost:8000` (FastAPI Swagger at `/docs`) and the frontend at `http://localhost:5173`.
