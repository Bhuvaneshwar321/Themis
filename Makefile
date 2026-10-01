.PHONY: setup db db-down dev-backend dev-frontend test

setup:
	cd backend && py -m venv .venv && .\.venv\Scripts\pip install -r requirements.txt
	cd frontend && npm install

db:
	docker compose up -d db

db-down:
	docker compose down

dev-backend:
	cd backend && .\.venv\Scripts\uvicorn app.main:app --reload --port 8000

dev-frontend:
	cd frontend && npm run dev

test:
	cd backend && .\.venv\Scripts\pytest
	cd frontend && npm run test -- --run
