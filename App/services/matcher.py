from langchain_mistralai import ChatMistralAI
import os
llm = ChatMistralAI(
                    api_key=os.getenv('MISTRAL_API_KEY'),
                    temperature=0.0,)

def match_resume(vector_db, job_description: str):
    result = vector_db.similarity_search_with_score(job_description, k=1)
    doc, distance = result[0]

    prompt = f"""
Compare the resume and job description.

Resume:
{doc.page_content}

Job Description
{job_description}

Return:
- Matching skills
- Missing skills
- Suitability score (0-100)
- Short explanation
"""

    explanation = llm.invoke(prompt).content

    return {
        "vector_distance": distance,
        "explanation": explanation,
        "metadata": doc.metadata
    }
