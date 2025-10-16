from langchain_community.document_loaders import PyPDFLoader , Docx2txtLoader , TextLoader , UnstructuredPowerPointLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import faiss
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain.schema import Document
import datetime
from langchain_huggingface import HuggingFaceEmbeddings
document = []

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")


embedding_dim = len(embeddings.embed_query("hello world"))
index = faiss.IndexFlatL2(embedding_dim)

vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

def extract_text_from_file(file_path,filename): 
    if filename.endswith('.pdf'):
        loader = PyPDFLoader(file_path)
    elif filename.endswith('.docx'):
        loader = Docx2txtLoader(file_path)
    elif filename.endswith('.pptx'):
        loader = UnstructuredPowerPointLoader(file_path)
    elif filename.endswith('.txt'):
        loader = TextLoader(file_path)
    else:
        # fallback or error handling
        raise ValueError("Unsupported file type: " + file_path)
    documents = loader.load()
    return "\n".join([doc.page_content for doc in documents])

def upload_document_vectorize(file_path,filename):
        
   
    content = extract_text_from_file(file_path,filename)
    # Compose metadata dict
    metadata = {
        "filename": filename,
        "upload_time": datetime.datetime.now().isoformat(),
        # add more fields as needed!
    }
    text_splitter =  RecursiveCharacterTextSplitter(
    chunk_size = 1500,
    chunk_overlap = 200,
    length_function = len
)
    doc = Document(page_content=content, metadata=metadata)
    # Split Document into chunks (each inherits metadata)
    docs = text_splitter.split_documents([doc])
    # Add docs (chunks with inherited metadata) to vector store
    vector_store.add_documents(docs)
    
# Retriever for retrieving the relavant documnets from the vector DB
retriever = vector_store.as_retriever(kwargs=3)