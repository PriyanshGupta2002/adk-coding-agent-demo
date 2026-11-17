# FastAPI Service

A simple FastAPI application featuring a health check endpoint.

## Setup & Installation

1. Create and activate a virtual environment (optional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   Or using `uv`:
   ```bash
   uv pip install -r requirements.txt
   ```

## Running the Application

Start the server using `uvicorn`:
```bash
uvicorn main:app --reload
```

## Endpoints

- **Root:** `GET /`
- **Health Check:** `GET /health`
- **API Docs:** `GET /docs`
