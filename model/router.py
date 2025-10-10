from fastapi import FastAPI , Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
from main import grammer_check_model , summarization_model

app = FastAPI()
@app.get("/")
def root():
    return FileResponse(Path(__file__).parent.parent / "frontend" / "index.html")
@app.post("/grammer_correction")
def grammer_correction(request: str = Body()):
    corrected_text = grammer_check_model(request)
    return {"corrected_text": corrected_text}

# SUMMARIZATION ENDPOINT
@app.post("/summarization")
def summarize(request: str = Body()):
    summary = summarization_model(request)
    return {"summary": summary}