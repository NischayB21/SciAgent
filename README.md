# SciAgent

SciAgent is an AI-powered multi-agent research assistant built with FastAPI.

It helps researchers discover scientific papers, analyze research publications using RAG (Retrieval-Augmented Generation), extract structured knowledge, identify research gaps, and generate future research recommendations using multiple intelligent AI agents.

---

## Features

- **Paper Search**: Query research papers from arXiv and OpenAlex.
- **PDF & Abstract Analysis**: Automated text extraction and chunking with RAG pipeline fallback.
- **Knowledge Extraction**: Vector embeddings indexing via ChromaDB.
- **Research Gap Detection**: Automated detection of open challenges and research gaps.
- **Future Recommendations**: Intelligent suggestion of novel research ideas and projects.
- **Multi-Agent Architecture**: Decoupled, modular agent design.
- **FastAPI REST API**: High-performance backend with interactive Swagger documentation.

---

## Tech Stack

- **Python 3.11+**
- **FastAPI & Uvicorn**
- **LangChain & LangGraph**
- **ChromaDB & Sentence Transformers**
- **OpenAlex & arXiv APIs**

---

## Project Structure

```
SciAgent/
├── backend/
│   ├── agents/
│   │   ├── analysis_agent/
│   │   ├── download_agent/
│   │   ├── gap_agent/
│   │   ├── knowledge_agent/
│   │   ├── recommendation_agent/
│   │   └── search_agent/
│   ├── api/
│   ├── core/
│   ├── data/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
├── README.md
└── .venv/
```

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd SciAgent/backend
   ```

2. **Set up Virtual Environment**
   ```bash
   python -m venv .venv
   ```

   **Activate environment:**
   - **Windows:** `.venv\Scripts\activate`
   - **Linux / macOS:** `source .venv/bin/activate`

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables (`backend/.env`)**
   ```env
   APP_NAME=SciAgent
   HOST=127.0.0.1
   PORT=8000
   LLM_MODEL=qwen3:8b
   CHROMA_DB=./backend/database/chromadb
   NEO4J_URI=bolt://localhost:7687
   NEO4J_USERNAME=neo4j
   NEO4J_PASSWORD=password
   ```

5. **Run the Server**
   ```bash
   python -m uvicorn main:app --reload
   ```

---

## API Documentation

Once the server is running, access the interactive Swagger documentation at:
```
http://127.0.0.1:8000/docs
```

---

## Endpoints

### `GET /`
Health check endpoint.
```json
{
  "message": "SciAgent Backend Running"
}
```

### `POST /research`
Searches research papers based on a given topic.

**Request:**
```json
{
  "topic": "Knowledge Graphs"
}
```

**Response:**
```json
{
  "count": 10,
  "papers": [
    {
      "title": "Grounding LLM Reasoning under Incomplete Graph Evidence",
      "authors": ["Jiaqi Li", "Fanghui Song"],
      "summary": "...",
      "published": "2026-06-29",
      "pdf_url": "https://arxiv.org/pdf/2606.30247v1",
      "source": "arXiv"
    }
  ]
}
```

### `POST /analyze`
Analyzes a selected paper using the multi-agent pipeline.

**Request:**
```json
{
  "paper": {
    "title": "Grounding LLM Reasoning under Incomplete Graph Evidence",
    "authors": ["Jiaqi Li", "Fanghui Song"],
    "summary": "...",
    "published": "2026-06-29",
    "pdf_url": "https://arxiv.org/pdf/2606.30247v1",
    "source": "arXiv"
  }
}
```

**Response:**
```json
{
  "paper": {},
  "analysis": {
    "summary": "...",
    "methods": [],
    "datasets": [],
    "metrics": [],
    "limitations": []
  },
  "knowledge": {
    "status": "success",
    "summary": "..."
  },
  "gaps": {
    "research_gaps": [],
    "future_work": [],
    "open_challenges": []
  },
  "recommendations": {
    "research_ideas": [],
    "improvements": [],
    "future_projects": []
  }
}
```

---

## Multi-Agent Workflow

```
User
 │
 ▼
POST /research
 │
 ▼
Search Agent (arXiv & OpenAlex)
 │
 ▼
Paper Selected
 │
 ▼
POST /analyze
 │
 ├──► Download Agent (Downloads PDF if available)
 ├──► Analysis Agent (Parses text, chunks, RAG analysis)
 ├──► Knowledge Agent (Embeddings & ChromaDB vector store)
 ├──► Gap Agent (Identifies limitations & research gaps)
 └──► Recommendation Agent (Generates novel ideas & future projects)
 │
 ▼
Structured JSON Response
```

---

## License

MIT License
