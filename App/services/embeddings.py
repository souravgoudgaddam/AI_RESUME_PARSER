from langchain_chroma import Chroma
from langchain_mistralai import MistralAIEmbeddings
from langchain_core.documents import Document
from App.models.resume_schema import Resume
import os
embeddings=MistralAIEmbeddings(api_key=os.getenv('MISTRAL_API_KEY'))



def store_resume_embedding(resume:Resume, persist_dir: str):
    text = f"""
Skills: {", ".join(resume.skills)}
Experience: {" ".join(resume.experience)}
Education: {" ".join(resume.education)}
"""

    doc = Document(
        page_content=text,
        metadata={
            "candidate_name": resume.name,
            "email": resume.email
        }
    )

    vector_db = Chroma.from_documents(
        documents=[doc],
        embedding=embeddings,
        persist_directory=persist_dir
    )

    return vector_db

