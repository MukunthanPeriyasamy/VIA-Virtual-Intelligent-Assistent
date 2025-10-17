from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from model.router import router

# Initialize FastAPI app
app = FastAPI(
    title="AI Services API",
    description="API for grammar correction, summarization, content creation, and RAG model",
    version="1.0.0"
)

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files for frontend
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

# Include API router
app.include_router(router, prefix="/api", tags=["AI Services"])

# Root endpoint - serve frontend
@app.get("/")
def root():
    return FileResponse(Path(__file__).parent / "frontend" / "index.html")

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "API is running"}
