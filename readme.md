***

# 🚀 AI Tools Service Platform (MVP)

<div align="center">
  <h3>Advanced AI Tools for Summarization, Correction, Formatting & RAG-based Chat</h3>
</div>

***

## 🌟 Project Highlights

> **This is an MVP (Minimum Viable Product)** — Expect rapid new releases & upgrades soon!

- **Text Summarization**: AI-powered, concise summaries for any content.
- **Grammar Correction**: Instantly fix grammar, typos, and awkward phrasing.
- **Content Formatting**: Automated text cleaning, multi-line splitting, and Markdown beautification.
- **Content Creation**: Generate original content with customizable prompts.
- **RAG Chat (Main Tool):** Retrieval-Augmented Generation Chat using advanced LLM and vector DB.
    - *Hybrid document and knowledge chat, multi-turn memory, enhanced response grounding.*


***

## 🔬 Core Technology

- **LLM Backbone**: [`Llama 3.3-70B-Versatile`](https://console.groq.com/docs/model/llama-3.3-70b-versatile) via [Groq](https://console.groq.com/)
    - Multilingual, 70B parameter model from Meta.
    - Sets a new standard for accuracy, efficiency, scalability, and reasoning
    - [Hugging Face Model Card](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct)
    - [Meta Official Card](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_3/)
    - **Instruction-tuned** and safe for general deployment (SFT + RLHF)
    - Real-time output with Groq’s ultra-fast inference (see [benchmarks](https://groq.com/blog/new-ai-inference-speed-benchmark-for-llama-3-3-70b-powered-by-groq))
    - > *Covers English, German, French, Italian, Portuguese, Hindi, Spanish, Thai & more; context window: 128K tokens.*

- **Framework:** [LangChain](https://www.langchain.com/)
    - Powerful prompt orchestration, RAG chaining, and tool-connectivity

- **Embeddings:** [Hugging Face Sentence Transformers](https://www.sbert.net/)
- **Vector Store:** [FAISS](https://github.com/facebookresearch/faiss) (high-speed vector similarity search)
- **API:** FastAPI ([docs](https://fastapi.tiangolo.com/))
- **Frontend:** Gemini AI + *prompt-chaining* methodology (“multi-step prompt engineering” — not a single-prompt UI!)
- **Prompt Orchestration:** `system_prompt.py` defines specialized system prompts per tool/module for highest control and task segmentation.

***

***

## ⚡ Quickstart

```bash
# 1. Create environment (Python venv, conda, or uv)
python -m venv venv         # or conda create -n ai-tools python=3.11
source venv/bin/activate    # (or activate your env via conda/uv)

# 2. Install all dependencies
pip install -r requirements.txt

# 3. Get your Groq API key
#    https://console.groq.com/keys

# 4. Create an `.env` file and add your API KEY:
echo "GROQ_API_KEY=sk-xxxxxxx" > .env

# 5. Launch the FastAPI server
uvicorn main:app --reload
```

***

## 🛠️ Usage

- **Web Interface**: UI powered by Gemini AI + advanced prompt chaining. Robust, user-friendly interactions for all AI tools.
- **API Access**: All tool-services exposed via `/summarize`, `/grammar_correction`, `/content_formatting`, `/content_creation`, `/rag_model_upload`, `/rag_model_chat` etc.
- **Ready for Chaining**: Easily connect one AI tool’s output into another — build flows!

***

## 🏗️ Architecture Overview

- **System Prompting**: `system_prompt.py` holds separate system prompts per tool, boosting guidance and safety.
- **RAG Implementation**: Hugging Face Sentence Transformers → FAISS → Llama 3.3-70B with LangChain for end-to-end question-answering grounded with context.
- **Prompt Chaining UI Engine**: Unlike basic one-prompt UI, our Gemini-driven UI is constructed in a sequence of guided, chained prompts (divide-and-conquer prompt methodology).

***

## 🚧 MVP Status — Roadmap

> *You are viewing the **first public MVP**! We’re iterating rapidly — expect frequent enhancements, new modules, and polish.*

***

## 🙌 Author & Connect

- **👤 Mukunthan Periyasamy**
- [LinkedIn Profile](https://www.linkedin.com/in/mukunthan004/)

***

**Cutting-edge LLM AI Tools. Lightning Fast. Modular. All Yours.**

***

