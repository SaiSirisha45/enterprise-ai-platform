# Enterprise AI Platform

An enterprise-grade AI platform built for BlackRoth that provides secure authentication, Role-Based Access Control (RBAC), Retrieval-Augmented Generation (RAG), enterprise knowledge management, semantic search, and AI-powered document assistance.

---

# Project Overview

The Enterprise AI Platform enables employees to securely interact with company knowledge using AI.

Key capabilities include:

- JWT Authentication
- Role-Based Access Control (RBAC)
- Audit Logging
- Enterprise Knowledge Base
- Document Processing Pipeline
- Embedding Generation
- ChromaDB Vector Database
- Semantic Search
- Enterprise Knowledge Center
- Docker Deployment

---

# Technology Stack

## Backend

- Python 3.14
- FastAPI
- Uvicorn

## Database

- PostgreSQL
- ChromaDB

## AI & RAG

- Sentence Transformers
- HuggingFace
- Chroma Vector Database

## Security

- JWT
- Passlib (bcrypt)
- RBAC
- Audit Logging

## Deployment

- Docker
- Docker Compose
- Redis

---

# Project Structure

```text
enterprise-ai-platform/

backend/
│
├── admin/
├── audit/
├── auth/
├── authentication/
├── chat/
├── evaluation/
├── rag/
├── security/
├── tests/

database/

docs/

storage/
├── documents/
├── chroma_db/

docker-compose.yml
Dockerfile
requirements.txt
README.md
```

---

# Completed Features

## Sprint 1

### Authentication

- JWT Login
- JWT Validation
- Password Hashing
- Token Verification

### Authorization

- RBAC
- Admin Access
- HR Access
- Employee Access

### Monitoring

- Audit Logs
- Request Logging

### Docker

- FastAPI
- PostgreSQL
- Redis

---

## Sprint 2

### Knowledge Base

- Document Upload
- PDF Support
- DOCX Support
- TXT Support
- Markdown Support

### Document Processing

- Text Extraction
- Chunking
- Metadata Extraction

### Embeddings

- Sentence Transformers
- MiniLM Embeddings
- Vector Generation

### Vector Database

- ChromaDB
- Persistent Storage
- Department Collections

### APIs

- Upload API
- Knowledge Base API
- Retrieval API
- Semantic Search API

### Administration

- Approval Queue
- Archive
- Version History

### Evaluation

- Retrieval Benchmark
- Chunk Evaluation
- Embedding Benchmark

---

## Enterprise Knowledge Center (Bonus)

Implemented:

- Multiple Upload
- Folder Management
- Department Collections
- Auto Embedding
- Approval Workflow
- Document Expiration
- Semantic Retrieval
- ChromaDB Integration

---

# Enterprise Architecture

```text
                User
                  │
                  ▼
         Authentication
                  │
                  ▼
          Authorization
                  │
                  ▼
        Enterprise API
                  │
       ┌──────────┴──────────┐
       │                     │
       ▼                     ▼
Knowledge Base         Audit Logger
       │
       ▼
Document Processor
       │
       ▼
Chunk Generator
       │
       ▼
Embedding Service
       │
       ▼
ChromaDB
       │
       ▼
Retriever
```

---

# Running Locally

## Clone Repository

```bash
git clone <repository-url>
cd enterprise-ai-platform
```

## Install Dependencies

```bash
pip install -r backend/requirements.txt
```

## Start FastAPI

```bash
uvicorn backend.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

---

# Docker

Build and start:

```bash
docker compose up --build
```

Stop:

```bash
docker compose down
```

---

# API Documentation

Swagger UI

```
http://127.0.0.1:8000/docs
```

---

# Sprint Progress

| Sprint | Status |
|---------|--------|
| Sprint 1 | ✅ Completed |
| Sprint 1 Bonus (Docker) | ✅ Completed |
| Sprint 2 | ✅ Completed |
| Sprint 2 Bonus | ✅ Completed |
| Sprint 3 |  In Progress |

---

# Future Enhancements

Sprint 3 will introduce:

- Hybrid Search
- Query Rewriting
- Cross Encoder Re-ranking
- Conversation Memory
- Context Builder
- Enterprise Chat API
- Citation Engine
- Hallucination Detection
- RAG Evaluation
- Enterprise Chat Dashboard

---

# Author

**D. Venkatesh**
**BR26AI9991**

Enterprise AI Platform Project

BlackRoth Enterprise AI Training