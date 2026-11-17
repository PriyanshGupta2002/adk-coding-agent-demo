from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="FastAPI Application",
    description="FastAPI service with health check endpoint",
    version="0.1.0"
)

class HealthResponse(BaseModel):
    status: str
    message: str

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the FastAPI service"}

@app.get("/health", response_model=HealthResponse, tags=["Health"])
def health_check():
    return HealthResponse(
        status="ok",
        message="Service is healthy"
    )
