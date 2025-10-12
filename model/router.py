from fastapi import FastAPI , Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
from main import grammer_check_model , summarization_model , content_creation_model , content_formatting_model

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.staticfiles import StaticFiles

app.mount("/frontend", StaticFiles(directory="../frontend"), name="frontend")

@app.get("/")
def root():
    return FileResponse(Path(__file__).parent.parent / "frontend" / "index.html")

# GRAMMAR CORRECTION ENDPOINT
@app.post("/grammer_correction")
def grammer_correction(request: str = Body()):
    corrected_text = grammer_check_model(request)
    return {"corrected_text": corrected_text}

# SUMMARIZATION ENDPOINT
@app.post("/summarization")
def summarize(request: str = Body()):
    summary = summarization_model(request)
    return {"summary": summary}

# CONTENT CREATION ENDPOINT
@app.post("/content_creation")
def content_creation(request: str = Body()):
    content = content_creation_model(request)
    return {"content": content}

# CONTENT FORMATTING ENDPOINT
@app.post("/content_formatting")
def content_formatting(request: str = Body()):
    formatted_content = content_formatting_model(request)
    return {"formatted_content": formatted_content}