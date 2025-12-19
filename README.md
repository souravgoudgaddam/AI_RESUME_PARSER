# AI Resume Parser & Job Matcher (GenAI + RAG)
#### 📌 Project Overview

#### This project is an end-to-end GenAI-powered Resume Parsing and Job Matching system.
#### It extracts structured information from unstructured resume PDFs, stores semantic embeddings in a vector database, and performs explainable resume–job matching using Large Language Models (LLMs).

#### The system is designed with a production-grade architecture, using FastAPI for backend services and ChromaDB for persistent vector storage 

#### Architecture
#### Resume PDF
   #### ↓
#### PDF Text Extraction (PyMuPDF)
   #### ↓
#### LLM-based Structured Parsing (LangChain + Pydantic)
   #### ↓
#### Vector Embeddings (Mistral Embeddings)
   #### ↓
#### ChromaDB (Persistent Vector Store)
   #### ↓
#### Semantic Job Matching + Explanation (LLM)

🛠️ Tech Stack

Backend: FastAPI

LLM: Mistral (ChatMistralAI)

Framework: LangChain

Vector DB: ChromaDB

Embeddings: Mistral Embeddings

Validation: Pydantic

PDF Parsing: PyMuPDF

UI: Swagger UI + Streamlit

Language: Python 3.11+

