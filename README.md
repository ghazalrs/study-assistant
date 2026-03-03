# Study Assistant

A RAG-powered study assistant where users create courses, upload PDFs, and ask questions grounded in their own materials with citations.

## Features
- Upload syllabus and lecture note PDFs
- Ask questions with RAG (retrieval-augmented generation) and source citations
- Optional Google Calendar integration for syllabus events
- Optional Gmail integration for drafting emails to instructors

## Tech Stack
- **Frontend:** Next.js (App Router), TypeScript, Tailwind, shadcn/ui, NextAuth (Google OAuth)
- **Backend:** FastAPI, PostgreSQL + pgvector, Celery + Redis, S3
- **Infra:** Docker, AWS ECS Fargate, RDS, ElastiCache

## Local Development

### Prerequisites
- Node 18+, Python 3.11+, Docker (optional)
- PostgreSQL with pgvector extension

### Backend
```bash
cd backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # fill in DATABASE_URL and other secrets
alembic upgrade head
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend
pnpm install
pnpm dev
```

### Environment Variables
| Variable | Description |
|---|---|
| `DATABASE_URL` | PostgreSQL connection string |
| `OPENAI_API_KEY` | For embeddings and completions |
| `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` | S3 access |
| `GOOGLE_CLIENT_ID` / `GOOGLE_CLIENT_SECRET` | OAuth + Calendar/Gmail |

## API Endpoints
| Method | Path | Description |
|---|---|---|
| GET/POST | `/courses` | List or create courses |
| DELETE | `/courses/{id}` | Delete a course |
| GET | `/courses/{id}/files` | List files for a course |
| DELETE | `/courses/{id}/files/{file_id}` | Delete a file |
| POST | `/courses/{id}/file/presign` | Get S3 presigned upload URL |
| POST | `/courses/{id}/file/complete` | Trigger ingestion after upload |
| POST | `/rag/query` | Ask a question with RAG |
| POST | `/calendar/preview` | Preview extracted calendar events |
| POST | `/calendar/commit` | Insert events to Google Calendar |
| POST | `/email/draft` | Generate email draft |
| POST | `/email/send` | Send a confirmed draft |
