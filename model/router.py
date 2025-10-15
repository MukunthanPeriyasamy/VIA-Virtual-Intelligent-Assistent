from fastapi import FastAPI , Body ,  File, UploadFile , HTTPException, status , APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path
from .main import grammer_check_model , summarization_model , content_creation_model , content_formatting_model
from .rag_model import Rag_Chain
from pydantic import BaseModel
from .vector_db import upload_document_vectorize
from .model import llm
import shutil
import os

router = APIRouter()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from fastapi.staticfiles import StaticFiles

app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

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

# RAG MODEL ENDPOINT
class QuestionRequest(BaseModel):
    question: str
    
@app.post("/rag_model_upload/")
async def upload(files: list[UploadFile] = File()):
    for file in files:
        temp_file_path = f"temp_{file.filename}"
        try:
            with open(temp_file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            upload_document_vectorize(temp_file_path, file.filename)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error processing file {file.filename}: {str(e)}"
            )
        finally:
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)

@app.post("/rag_model_chat/")     
def chat(res: QuestionRequest):
    result = Rag_Chain(res.question, llm)
    return {"answer": result}