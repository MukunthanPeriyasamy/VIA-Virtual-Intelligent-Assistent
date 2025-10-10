from model import llm
from system_prompts import grammer_model_system_prompt , summarization_model_system_prompt
from langchain_core.prompts import ChatPromptTemplate


# GRAMMER CORRECTION MODEL

grammer_system_prompt = ChatPromptTemplate.from_template(grammer_model_system_prompt)

grammer_chain = grammer_system_prompt | llm

def grammer_check_model(passage: str) -> str:
    response = grammer_chain.invoke({"passage": passage})
    return response.content


# SUMMARIZATION MODEL

summarizarion_system_prompt = ChatPromptTemplate.from_template(summarization_model_system_prompt)
summarization_chain = summarizarion_system_prompt | llm

def summarization_model(content: str) -> str:
    response = summarization_chain.invoke({"content": content})
    return response.content