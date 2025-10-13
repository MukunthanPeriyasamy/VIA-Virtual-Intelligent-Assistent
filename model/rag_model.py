from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnablePassthrough
from langchain.prompts import PromptTemplate
from vector_db import retriever
from system_prompts import rag_model_system_prompt as system_prompt
from model import llm


#Intializing the Output Parser
output_parser = StrOutputParser()

document = []


# Building the RAG chain
def format_docs_with_metadata(docs):
    formatted_docs = []
    for doc in docs:
        content = doc.page_content
        metadata = doc.metadata  # should include filename, upload time, etc.
        
        doc_info = f"Document Name: {metadata.get('filename', 'Unknown')}\n"
        doc_info += f"Upload Time: {metadata.get('upload_time', 'Unknown')}\n"
        doc_info += f"Content: {content}\n"
        
        formatted_docs.append(doc_info)
    return "\n\n".join(formatted_docs)

def Rag_Chain(question, llm):
    template = system_prompt
    prompt = PromptTemplate(template=template, input_variables=["context_with_metadata", "question"])
    docs = retriever.get_relevant_documents(question)
    context_with_metadata = format_docs_with_metadata(docs)
    
    chain = (
        {'context_with_metadata': RunnablePassthrough(), 'question': RunnablePassthrough()}
        | prompt
        | llm
        | output_parser     
    )
    rag_response = chain.invoke({
        "context_with_metadata": context_with_metadata,
        "question": question
    })
    return rag_response