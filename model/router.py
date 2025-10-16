from fastapi import Body, File, UploadFile, HTTPException, status, APIRouter
from pydantic import BaseModel
from .main import grammer_check_model, summarization_model, content_creation_model, content_formatting_model
from .rag_model import Rag_Chain
from .vector_db import upload_document_vectorize
from .model import llm
import shutil
import os

# Initialize the APIRouter
router = APIRouter()

# Pydantic Models
class QuestionRequest(BaseModel):
    question: str

# GRAMMAR CORRECTION ENDPOINT
@router.post("/grammer_correction")
def grammer_correction(request: str = Body()):
    corrected_text = grammer_check_model(request)
    return {"corrected_text": corrected_text}

# SUMMARIZATION ENDPOINT
@router.post("/summarization")
def summarize(request: str = Body()):
    summary = summarization_model(request)
    return {"summary": summary}

# CONTENT CREATION ENDPOINT
@router.post("/content_creation")
def content_creation(request: str = Body()):
    content = content_creation_model(request)
    return {"content": content}

# CONTENT FORMATTING ENDPOINT
@router.post("/content_formatting")
def content_formatting(request: str = Body()):
    formatted_content = content_formatting_model(request)
    return {"formatted_content": formatted_content}

# RAG MODEL UPLOAD ENDPOINT
@router.post("/rag_model_upload/")
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
    
    return {"message": "Files uploaded and processed successfully"}

# RAG MODEL CHAT ENDPOINT
@router.post("/rag_model_chat/")
def chat(res: QuestionRequest):
    result = Rag_Chain(res.question, llm)
    return {"answer": result}
