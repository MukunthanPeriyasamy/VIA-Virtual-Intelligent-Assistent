from model import llm
from system_prompts import content_formatting_model_system_prompt, grammar_model_system_prompt , summarization_model_system_prompt , content_creation_model_system_prompt
from langchain_core.prompts import ChatPromptTemplate


# GRAMMER CORRECTION MODEL

grammer_system_prompt = ChatPromptTemplate.from_template(grammar_model_system_prompt)

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


# CONTENT CREATION MODEL

content_creation_system_prompt = ChatPromptTemplate.from_template(content_creation_model_system_prompt)
content_creation_chain = content_creation_system_prompt | llm
def content_creation_model(content: str) -> str:
    response = content_creation_chain.invoke({"input": content},temperature=0.7)
    return response.content

# CONTENT FORMATTING MODEL
content_formatting_system_prompt = ChatPromptTemplate.from_template(content_formatting_model_system_prompt)
content_formatting_chain = content_formatting_system_prompt | llm
def content_formatting_model(passage: str) -> str:
    response = content_formatting_chain.invoke({"content": passage})
    return response.content