from fastapi import FastAPI , Body
from main import grammer_check_model , summarization_model

app = FastAPI()
@app.get("/")
def root():
    return {"message": "Welcome to the Grammar Correction AI. Use the /correct endpoint to submit text for grammar correction."}

# GRAMMER CORRECTION ENDPOINT
@app.post("/grammer_correction")
def grammer_correction(request: str = Body()):
    corrected_text = grammer_check_model(request)
    return {"corrected_text": corrected_text}

# SUMMARIZATION ENDPOINT
@app.post("/summarization")
def summarize(request: str = Body()):
    summary = summarization_model(request)
    return {"summary": summary}